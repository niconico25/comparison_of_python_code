import funcscale
import random


def comparison():
    funcscale.function_list = [
        reverse,
        reverse_exception,
        reverse_function
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(6)
    ]
    funcscale.compare()


def reverse(sequence):
    iterable = Reverse(sequence)
    # for statement
    lst = []
    for element in iterable:
        lst.append(element)
    return lst


def reverse_exception(sequence):
    iterable = ReverseException(sequence)
    # for statement
    lst = []
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
        except StopIteration:
            break
        lst.append(element)
    return lst


def reverse_function(sequence):
    iterable = ReverseFunction(sequence)
    # for statement
    lst = []
    iterator = iter(iterable)
    while has_next(iterator):
        element = next(iterator)
        lst.append(element)
    return lst


class Reverse(object):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index -= 1
        if self._index >= - len(self._sequence):
            return self._sequence[self._index]
        else:
            raise StopIteration


ReverseException = Reverse


class ReverseFunction(object):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index -= 1
        return self._sequence[self._index]

    def __has_next__(self):
        return self._index > - len(self._sequence)


def has_next(iterator):
    return iterator.__has_next__()


comparison()
