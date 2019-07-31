import datetime as dt


def get_or_none(model, pk):
    if not isinstance(model, object):
        raise ValueError('Invalid model value: need pass object')
    if not pk:
        return None
    instance = model(pk)

    # Two case: object contain exists() method or we try run hash_exist
    if hasattr(instance, 'exists'):
        return instance if instance.exists() else None
    return instance if instance.hash_exist() else None


def now():
    return dt.datetime.now()
