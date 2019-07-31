import logging

import falcon

from api.hooks import extract_fields
from models import Member
from models.utils import get_or_none
from rest.errors import PublicException
from serializers.member import MemberSchema


def extract_member(req, resp, resource, params):
    #pylint: disable=unused-argument
    pk = params.get('pk')
    member = get_or_none(Member, pk)
    if not member:
        raise PublicException('Member is not found', code=404)
    params['member'] = member


class MemberResource:
    @falcon.before(extract_fields)
    @falcon.before(extract_member)
    def on_get(self, req, resp, member, fields, **kwargs):
        #pylint: disable=unused-argument, no-self-use
        logger.debug('Get %s', member)
        ser = MemberSchema(only=fields)
        resp.response = ser.dump(member)

    def on_put(self, req, resp, pk, **kwargs):
        #pylint: disable=unused-argument, no-self-use
        if not pk.isdigit():
            raise PublicException('Member\'s pk must be a number')
        params = {}
        req.get_param_as_int('age', store=params)
        req.get_param('name', required=True, store=params)
        req.get_param('email', required=True, store=params)

        member = get_or_none(Member, pk)
        if member:
            raise PublicException('Member already exists')
        member = Member.new(pk, **params)
        logger.debug('%s has been created', member)
        resp.response = dict(created=True)

    @falcon.before(extract_member)
    def on_post(self, req, resp, member, **kwargs):
        #pylint: disable=unused-argument, no-self-use
        params = {}
        req.get_param_as_int('age', store=params)
        req.get_param('name', store=params)
        req.get_param('email', store=params)
        for k, v in params.items():
            if v is not None:
                setattr(member, k, v)
        logger.debug('%s has been modified', member)
        ser = MemberSchema()
        resp.response = ser.dump(member)


logger = logging.getLogger(__name__)
