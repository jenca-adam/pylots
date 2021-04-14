import os
import redis
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
from werkzeug.serving import run_simple

class _app(object):

    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        self.urls={}
    def path(self,path):
        def decor(fun):
            self.urls[path]=fun
        return decor
    def dispatch_request(self, request):
        if request.environ['REQUEST_URI']in self.urls:
            return Response(self.urls[request.environ['REQUEST_URI']](request),mimetype='text/html')
        return Response('<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>',status=404,mimetype='text/html')


    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)
    def run(self,port):
        run_simple('127.0.0.1', port , self, use_debugger=True, use_reloader=True)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def App(redis_host='localhost', redis_port=6379, with_static=True):
    app = _app({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

