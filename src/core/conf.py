import os

import yaml


def load_settings(settings_path):
    with open(settings_path, 'r') as f:
        conf_string = ''.join(f.readlines())

    for k, v in os.environ.items():
        conf_string = conf_string.replace('$%s' % k.upper(), str(v))

    conf = yaml.load(conf_string, Loader=yaml.FullLoader)
    settings.load(conf)
    return settings


class _LazySettings:
    def __init__(self, data):
        self.data = data

    def load(self, data):
        self.data = data

    def __getattr__(self, item):
        if item not in self.data:
            raise KeyError('Invalid settings key %s' % (item, ))
        val = self.data[item]
        if isinstance(val, (dict, list,)):
            return _LazySettings(val)
        return val

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def get(self, key, default=None):
        if key not in self.data:
            return default
        return self[key]

    def keys(self):
        return self.data.keys()

    def items(self):
        return self.data.items()

    def values(self):
        return self.data.values()

    # def __contains__(self, key):
    #     pass


settings = _LazySettings(dict())
