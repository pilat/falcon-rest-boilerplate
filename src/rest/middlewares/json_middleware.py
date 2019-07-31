class JsonMiddleware:
    def process_request(self, req, resp, **kwargs):
        #pylint: disable=unused-argument
        if req.client_accepts_json and req.method in ('POST', 'PUT') and \
           req.content_type == 'application/json':
            for k, v in req.media.items():
                req._params[k] = v
