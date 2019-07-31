from falcon_cors import CORS
from core.conf import settings


_cors = CORS(allow_origins_list=settings.FALCON_ALLOW_ORIGINS,
             allow_all_methods=True)

cors_middleware = _cors.middleware
