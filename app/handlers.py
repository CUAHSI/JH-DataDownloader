#!/usr/bin/env python3


import os
import json
import subprocess
import tornado.auth
import tornado.web
from tornado import gen 
from tornado.log import app_log
from tornado.log import enable_pretty_logging


import environment as env

enable_pretty_logging()

import db

#import sqldata
#sql = sqldata.Connect(env.sqldb)
#sql.build()


class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("index.html", title="")

class SuccessHandler(tornado.web.RequestHandler):

    def get(self, username):
        pgdb = db.DB()
        pgdb.insert(username)
        self.render("success.html", title="", dat={'username': username})

#class ErrorHandler(tornado.web.RequestHandler):
#
#    def get(self):
#        import pdb; pdb.set_trace()
#        self.render("error.html", title="", dat={'username': 'test'})

class SubmitHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def post(self):

        # get post argument
        username = self.get_body_argument("username")

        # check that username exists in cluster 
        # and get disk info
        app_log.info(f'checking that {username} exists')
        exe = os.path.join(env.utils, 'get-pvc-for-user.sh')
        cmd = [exe,
               username,
               env.cluster_namespace]
        app_log.info(cmd)
        rc, output, err = run_bash(env.utils,
                               cmd)
        output = output.decode().strip()
        err = err.decode().strip()
        if rc == 0:
            # success
            pvc_data = json.loads(output)
            app_log.info(pvc_data)

        else:
            # error
            app_log.error(err)
            
            # redirect to error page
            self.render('error.html', dat={'error-msg': err})


        # attach, mount, and compress data
        app_log.info(f'attaching disk for {username}')
        exe = os.path.join(env.utils, 'attach-disk.sh')
        cmd = [exe,
               username,
               pvc_data['HDD'],
               env.server_zone,
               env.server_name,
               env.data_dir]
        app_log.info(cmd)
        rc, output, err = run_bash(env.utils,
                               cmd)
        output = output.decode().strip()
        err = err.decode().strip()
        if rc != 0:
            # error
            app_log.error(err)
            
            # redirect to error page
            self.render('error.html', dat={'error-msg': err})

        # detach disk and clean up
        app_log.info(f'detaching disk and cleaning up')
        exe = os.path.join(env.utils, 'detach-disk.sh')
        cmd = [exe,
               username,
               env.server_name,
               env.data_dir]
        app_log.info(cmd)
        rc, output, err = run_bash(env.utils,
                               cmd)
        output = output.decode().strip()
        err = err.decode().strip()
        if rc != 0:
            # error
            app_log.error(err)
            
            # redirect to error page
            self.render('error.html', dat={'error-msg': err})

        # redirect to download page
        self.redirect(f'/success/{username}')


def run_bash(cwd, cmd):

    print(' '.join(cmd))
    p = subprocess.Popen(cmd,
                         cwd=cwd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output, err = p.communicate()
    app_log.info(output)
    app_log.info(err)
    return p.returncode, output, err


