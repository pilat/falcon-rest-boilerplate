from .cors_middleware import cors_middleware
from .json_middleware import JsonMiddleware
from .logger_middleware import LoggerMiddleware
from falcon_multipart.middleware import MultipartMiddleware


middleware = [
    cors_middleware,
    LoggerMiddleware(),
    JsonMiddleware(),  # recognize JSON
    MultipartMiddleware()
]
