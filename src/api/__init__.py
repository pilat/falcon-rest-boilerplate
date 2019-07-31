from api.member import MemberResource
from core.conf import settings


def on_ready(app):
    member = MemberResource()
    app.rest.add_route('/member/{pk}', member)
