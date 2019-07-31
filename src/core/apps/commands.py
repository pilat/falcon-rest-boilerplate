import argparse
import sys


class Commands:
    """
    It's an aystem application available as "commands". It has "register"
    method to expose your command to CLI. For example:

      app.commands.register('hello', say_hello_handler)
      def say_hello_handler(app):
          # You may use argparse here
          pass
    """
    def __init__(self, app):
        self._app = app
        self._commands = {}

    def run(self):
        commands_list = []
        for name, (_, description) in self._commands.items():
            commands_list.append('  %s - %s' % (name, description) \
                if description is not None else '  %s' % name)

        parser = argparse.ArgumentParser(
            description='Application runner',
            usage='app.py <command> [<args>]\n\nAvailable commands:\n%s' % \
                '\n'.join(commands_list))
        parser.add_argument('command', type=str, help='Subcommand to run')

        # Call command was registered during initialization
        args = parser.parse_args(sys.argv[1:2])
        command = self._commands.get(args.command)
        if not command:
            print('Unrecognized command. Use app.py --help')
            exit(1)
        command[0](self._app)

    def register(self, command, handler, description=None):
        if command in self._commands:
            raise ValueError('Command %s has already exists' % command)
        self._commands[command] = (handler, description)


def on_ready(app):
    commands = Commands(app)
    app.export('commands', commands)
