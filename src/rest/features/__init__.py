import falcon

from .json_response import JsonResponseFeature


class CustomRequest(falcon.request.Request):
    def client_prefers(self, media_types):
        return 'application/json'


class CustomResponse(falcon.response.Response, JsonResponseFeature):
    pass
