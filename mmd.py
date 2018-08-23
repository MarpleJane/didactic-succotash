#coding: utf8
import logging

import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer

from config.urls import urls


PORT = "8889"
def main():
    application = tornado.web.Application(urls)
    server = HTTPServer(
        application,
        xheaders=True,
        max_body_size=1024*1024*1024
    )
    server.bind(PORT)
    server.start(1)
    logging.warn("Start application from port [%s]", PORT)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


