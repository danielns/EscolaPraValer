from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app
import tornado.options
import sys 

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8484)

args = sys.argv
args.append("--log_file_prefix=/home/escolapravalerco/EscolaPraValer/site.log")
tornado.options.parse_command_line(args)

#tornado.options.options['log_file_prefix'].set('')

IOLoop.instance().start()
