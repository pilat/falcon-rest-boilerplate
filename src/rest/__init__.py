import argparse
import logging
import sys
from wsgiref import simple_server

import falcon

from rest.features import CustomResponse

from .errors import apply_error_handlers
from .features import CustomRequest
from .middlewares import middleware


class NoLoggingWSGIRequestHandler(simple_server.WSGIRequestHandler):
    def log_message(self, _format, *args):
        pass


def run_http_server(app):
    parser = argparse.ArgumentParser(description='Run an HTTP Server')
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args(sys.argv[2:])

    logger.info('Run HTTP server at %s:%i', args.host, args.port)
    httpd = simple_server.make_server(
        args.host, args.port, app.rest,
        handler_class=NoLoggingWSGIRequestHandler)
    httpd.serve_forever()


def on_ready(app):
    falcon_app = falcon.API(request_type=CustomRequest,
                            response_type=CustomResponse,
                            middleware=middleware)
    apply_error_handlers(falcon_app)
    app.export('rest', falcon_app)

    app.commands.register('rest', run_http_server, 'Run an HTTP Server')


logger = logging.getLogger(__name__)
