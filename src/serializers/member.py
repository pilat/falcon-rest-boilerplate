from marshmallow import fields

from . import BaseSchema


class MemberSchema(BaseSchema):
    id = fields.Integer()
    ts = fields.DateTime()
    name = fields.String()
    age = fields.Integer()
    email = fields.String()
