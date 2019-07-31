import logging

from dotenv import load_dotenv

from .conf import load_settings
from .manager import AppManager

SYS_APPS = (
    'core.apps.commands',
    'core.apps.logger',
)


def execute_from_command_line():
    load_dotenv('.env')  # Setup default envinronment
    load_settings('settings.yaml')  # Load settings. It's globally

    app = AppManager()
    app.discover(SYS_APPS)  # Find that modules, call on_ready()
    app.autodiscover()  # The same based on "applicaions" setting
    app.commands.run()  # Start CLI


logger = logging.getLogger(__name__)
