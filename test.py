from lexon import *


@lex
def echo(msg:str) -> None:
    print(f'echo: {msg}')


@lex
def no_kwargs(**kwargs) -> None:
    print("this will never get called")


@lex
def do(param1, param2=None) -> None:
    print("doing a thing")
    print(param1)
    if param2: print(param2)


if __name__ == '__main__':
    lexon()