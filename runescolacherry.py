#!/usr/bin/env python

from flask import Flask
import cherrypy
from paste.translogger import TransLogger

from app import app


def run_server():
    # Enable WSGI access logging via Paste
    app_logged = TransLogger(app)

    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app_logged, '/')

    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload_on': True,
        'log.error_file': 'site.log',
        'environment': 'production',
        'log.screen': True,
        'server.socket_port': 8484,
        'server.socket_host': '0.0.0.0',
        'server.thread_pool': 30
        #'server.socket_host': '198.50.106.250'
    
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == "__main__":
    run_server()

