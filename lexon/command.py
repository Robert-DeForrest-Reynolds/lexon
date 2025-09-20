from typing import Callable

class Command:
    name:str
    function:Callable
    def __init__(_, function:Callable) -> None:
        _.name = function.__name__
        _.function = function
        _.arg_count = function.__code__.co_argcount
        _.params = function.__code__.co_varnames

    
    def call(_, *args):
        if len(args) > _.arg_count:
            print(f'Too many arguments passed to {_.name}')
            return
        try:
            _.function(*args)
        except TypeError as e:
            missing_param = e.__str__().split(": ")[1].replace("'", "")
            print(f'{_.name} is missing required argument(s): {missing_param}')