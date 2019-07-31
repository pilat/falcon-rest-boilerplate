import logging
import uuid

import falcon


__all__ = [
    "PublicException", "apply_error_handlers"
]


class ExtendedHTTPError(falcon.HTTPError):
    # https://falcon.readthedocs.io/en/stable/api/errors.html
    def __init__(self, status, title=None, description=None, headers=None,
                 href=None, href_text=None, code=None, extra=None, **kwargs):
        self.kwargs = kwargs
        self.extra = extra
        # super().__init__(*args, **kwargs)
        super().__init__(status, title, description, headers, href,
                         href_text, code)

    def to_dict(self, obj_type=dict):
        obj = obj_type()

        for k, v in self.extra.items():
            obj[k] = v

        obj['code'] = self.code or 500
        obj['message'] = self.title
        if self.description is not None:
            obj['description'] = self.description

        return dict(error=obj)


def generic_handler(req, resp, ex, params):
    code = 500
    title = 'Internal Server Error'
    report_id = uuid.uuid4().hex[:16]
    extra = dict(report_id=report_id)

    if isinstance(ex, (PublicException,)):
        logger.warning('PublicException #%s', report_id, exc_info=ex)
        extra.update(ex.kwargs)
        code = int(ex.kwargs.get('code', 500))
        title = ex.message
    else:
        logger.error('Exception #%s', report_id, exc_info=ex)

    status = getattr(falcon, 'HTTP_%i' % code, falcon.HTTP_500)
    raise ExtendedHTTPError(status, title, code=code, extra=extra, **params)


def apply_error_handlers(app):
    app.add_error_handler(Exception, generic_handler)


class PublicException(Exception):
    """
    Messages of that type will be sent to client. You could also
    use additional fields which will be transferred.
    """
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs
        self.kwargs.setdefault('code', 400)
        super().__init__(message)


logger = logging.getLogger(__name__)
