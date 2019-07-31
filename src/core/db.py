import redis
from core.conf import settings


_db = {}


def get_redis(name='default', decode_responses=True) -> 'redis.StrictRedis':
    key = '%s_%s' % (name, 'decode' if decode_responses else 'not_decode')
    if key not in _db:
        conf = settings.get('redis_%s' % name)
        if not conf:
            raise ValueError('Database %s is not found' % name)
        _db[key] = redis.StrictRedis(decode_responses=decode_responses,
                                     **conf)
    return _db[key]
