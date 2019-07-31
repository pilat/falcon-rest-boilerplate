import json
import logging


class JsonResponseFeature:  # (falcon.response.Response):
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, val):
        self._response = val
        self.body = json.dumps(self._response)


logger = logging.getLogger(__name__)
