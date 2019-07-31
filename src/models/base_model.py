import uuid

from astra import models as am

from core.db import get_redis


class RAModel(am.Model):
    def get_db(self):
        return get_redis()

    def get_key_prefix(self):
        return 'astra::%s' % self.__class__.__name__.lower()[1:]

    @property
    def id(self):
        return self.pk

    @classmethod
    def make_id(cls):
        return uuid.uuid4().hex

    def __str__(self):
        return '[%s %s]' % (self.__class__.__name__[1:], self.pk)
