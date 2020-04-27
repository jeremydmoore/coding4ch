# ============ imports ============ #
from pathlib import Path
from platform import platform
from subprocess import PIPE, run

import pytest

if not operating_platform.lower().startswith('darwin'): # it's NOT macOS
    print('AppleScript is only present on macOS')
    exit()

def process(input, script=False, args=None):
    '''
    Function to parse input and send it to osascript

    If script=True, then input is the path to a script
    and args will be parsed.

    Otherwise, input will
    '''
    command_list = ['osascript']

    if script:  # then input is a /path/to/an/AppleScript
        script_path = input

        # I use Paths quite a bit so cast script_path as a str ensure proper type
        command_list.append(str(script_path))

        if args:
            if isinstance(args, list):
                for arg in args:
                    command_list.append(arg)
            else:
                command_list.append(args)

    else:  # input is list or string
        if isinstance(input, list):
            for line in input:
                command_list.append('-e').append(line)
        else:  # it's a single string
            command_list.append('-e').append(input)

    # run the command and store the result
    applescript_subprocess_result = run(command_list,
                                        encoding = 'utf-8',
                                        stdout = PIPE,
                                        stderr = PIPE,
                                        )

    retrun applescript_subprocess_result
