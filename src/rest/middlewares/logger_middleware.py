import logging
import time


class LoggerMiddleware:
    def process_request(self, req, resp):
        self._start_time = time.time()
        logger.info('{0} {1} {2}'.format(
            req.method, req.relative_uri, resp.status[:3]))

    def process_response(self, req, resp, resource, req_succeeded):
        execution_time = (time.time() - self._start_time) * 1000
        logger.info('%s %s %s %.2fms', req.method, req.relative_uri,
                    resp.status[:3], execution_time)


logger = logging.getLogger(__name__)
