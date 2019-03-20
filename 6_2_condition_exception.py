import funcscale
import random


def comparison():
    funcscale.function_list = [
        reverse_exception,
        reverse_function
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(6)
    ]
    funcscale.str_argument_list = [
        f'([random.randint(0, 10**n - 1) for i in range(10**n)], ),'
        for n in range(6)
    ]
    funcscale.compare()


def reverse_exception(sequence):
    iterable = ReverseException(sequence)
    # Executing a samething with list comprehension by using while statement.
    # lst = [element for element in iterable]
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
    # Executing a samething with list comprehension by using while statement.
    # lst = [element for element in iterable]
    lst = []
    iterator = iter(iterable)
    while has_next(iterator):
        element = next(iterator)
        lst.append(element)
    return lst


class ReverseException:
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


class ReverseFunction:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index -= 1
        return self._sequence[self._index]

    def _has_next(self):
        return self._index > - len(self._sequence)


def has_next(iterator):
    return iterator._has_next()


#
#
#
if __name__ == '__main__':
    comparison()
