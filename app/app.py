#!/usr/bin/env python3


import os
import sys
import logging
import tornado.web
from tornado import httpserver
from tornado.ioloop import IOLoop

# import 'logs' before other modules
# to ensure logs are configured properly
import logs

import handlers
import environment as env


class Application(tornado.web.Application):
    def __init__(self):
        endpoints = [
            (r"/", handlers.IndexHandler),
            (r'/user-submit', handlers.SubmitHandler),
            (r'/success/(.*)', handlers.SuccessHandler),
#            (r'/error', handlers.ErrorHandler),
            (r"/data/(.*)", tornado.web.StaticFileHandler,
                            {"path": env.data_dir}),
        ]
        settings = {
            "debug": env.debug,
            "static_path": env.static_path,
            "template_path": env.template_path,
        }
        tornado.web.Application.__init__(self, endpoints, **settings)


def main():

    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)

    # initialize logs
    applogs = logs.Logs()

    http_server.listen(env.port, address=env.address)
    print('\n'+'-'*60)
    print('server listening on %s:%s' % (env.address, env.port))
    print('-'*60+'\n')
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
