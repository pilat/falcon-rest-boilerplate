from importlib import import_module

from .conf import settings


class AppManager:
    def __init__(self):
        self._exports = {}

    def autodiscover(self):
        self.discover(settings.applications)

    def discover(self, applications):
        ready_handlers = []
        for app in applications:
            module = import_module(app)
            handler = getattr(module, 'on_ready', None)
            if handler:
                ready_handlers.append(handler)
        for on_ready in ready_handlers:
            on_ready(self)

    def export(self, name, value):
        if name in self._exports:
            raise ValueError('%s has already exported' % name)
        self._exports[name] = value

    def __getattr__(self, name):
        return self._exports.get(name)
