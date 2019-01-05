import funcscale


def comparison():
    function_list = [
        next_condition,
        next_exception
    ]
    argument_list = [
        ((list(range(10**n)),), {})
        for n in range(7)
    ]

    def setup(function, argument):
        return '\n'.join((
            'from __main__ import ' + function.__name__,
            'from __main__ import Reverse',
            'Reverse.__next__ = ' + function.__name__,
            'reverse = Reverse' + funcscale.repr_argument(argument)
        ))

    def stmt(function, argument):
        return '[element for element in reverse]'

    # Set parameters.
    funcscale.function_list = function_list
    funcscale.argument_list = argument_list
    funcscale.stmt = stmt
    funcscale.setup = setup

    # Execute.
    funcscale.compare()


class Reverse(object):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self


def next_condition(self):
    self._index -= 1
    if self._index >= - len(self._sequence):
        return self._sequence[self._index]
    else:
        raise StopIteration


def next_exception(self):
    self._index -= 1
    try:
        return self._sequence[self._index]
    except IndexError:
        raise StopIteration


comparison()
