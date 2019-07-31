import os
import sys


sys.path.insert(0, os.path.join(os.getcwd(), 'src'))


if __name__ == '__main__':
    try:
        from core.entrypoint import execute_from_command_line
    except ImportError as exc:
        raise ImportError('Couldn\'t import Entrypoint Application') from exc

    execute_from_command_line()

