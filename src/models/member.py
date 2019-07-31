from astra import models as am

from .base_model import RAModel
from .utils import now


class _Member(RAModel):
    ts = am.DateTimeHash()
    name = am.CharHash()
    email = am.CharHash()
    age = am.IntegerHash()

    @staticmethod
    def new(pk, **kwargs):
        member = _Member(pk=pk, ts=now(), **kwargs)
        return member
