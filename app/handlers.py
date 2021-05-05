#!/usr/bin/env python3

import tornado.auth
import tornado.web
from tornado.log import app_log
from tornado.log import enable_pretty_logging


import environment as env

enable_pretty_logging()

#import sqldata
#sql = sqldata.Connect(env.sqldb)
#sql.build()



class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("index.html", title="")

class SubmitHandler(tornado.web.RequestHandler):

    def post(self):

        self.render("user-submit.html")

