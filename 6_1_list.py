import funcscale


def comparison():
    function_list = [
        list_iterator,
        iterator,
        generator
    ]
    argument_list = [
        (([None] * 10**n, ), {}) for n in range(6)
    ]

    def setup(function, argument):
        return '\n'.join((
            'from __main__ import ' + function.__name__,
            'from __main__ import Container',
            'container = Container' + funcscale.repr_argument(argument),
            'Container.__iter__ = ' + function.__name__
        ))

    def stmt(fucntion, argument):
        return '[element for element in container]'

    funcscale.function_list = function_list
    funcscale.argument_list = argument_list
    funcscale.stmt = stmt
    funcscale.setup = setup

    funcscale.compare()


#
#
#
def sample():
    Container.__iter__ = list_iterator
    # Container.__iter__ = iterator
    # Container.__iter__ = generator

    print('# 1) for statement')
    container = Container(('Yaruo', 'Yaranaio', 'Yarumi'))
    for element in container:
        print(element)

    print('# 2) built-in function taking itrable object')
    container_a = Container(('hello', 'nihao', 'hola'))
    container_b = Container(('nihao', 'holda', 'hello'))
    print(set(container_a) == set(container_b))  # True

    print('# 3) you do not need implement list method.')
    print(list(container))


#
#
#
class Container(object):
    def __init__(self, list_):
        self._list = list_

    def __iter__(self):
        raise NotImplementedError


class ListIterator(object):
    def __init__(self, list_):
        self._list = list_
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            element = self._list[self._index]
            self._index = self._index + 1
            return element
        except IndexError:
            raise StopIteration
        """
        # try stmt is faster than if stmt in this case.
        if self._index < len(self._list):
            element = self._list[self._index]
            self._index = self._index + 1
            return element
        else:
            raise StopIteration
        """


def list_iterator(self):
    return iter(self._list)


def iterator(self):
    return ListIterator(self._list)


def generator(self):
    index = 0
    while True:
        try:
            yield self._list[index]
        except IndexError:
            break
        else:
            index = index + 1


#
#
#
if __name__ == "__main__":
    comparison()
    sample()
