# smile away, we're alive today

from sys import argv
from typing import Callable
from inspect import Signature, signature, Parameter

from .command import Command

__all__ = ["lexon", "lex"]


commands:dict[str,Command] = {}


def help() -> None:
    help_string = ""
    for name, command in commands.items():
        help_string += f"""{name} {' '.join([f'<{param}>' for param in command.params])}\n"""
    print(help_string)


def lex(function:Callable) -> None:
    sig:Signature = signature(function)
    for param in sig.parameters.values():
        if param.kind == Parameter.VAR_KEYWORD:
            raise TypeError(f"`{function.__name__}` command cannot take in **kwargs")
    commands.update({function.__name__:Command(function)})


def lexon() -> None:
    if len(argv) <= 1:
        help()
        exit(1)
    else:
        try:
            commands[argv[1]].call(*argv[2:])
        except KeyError:
            print("Command does not exist")