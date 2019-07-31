from marshmallow import Schema, post_dump, utils
from astra import models as am


class BaseSchema(Schema):
    @post_dump
    def remove_none_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if value is not None
        }

    def get_attribute(self, obj, attr, default):
        value = utils.get_value(obj, attr, default)

        if isinstance(value, am.SortedSet):
            value = value['-inf':'+inf']

        return value
