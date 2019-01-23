import funcscale
import random


def comparison():
    # Create parameters.
    function_list = [
        list_iterator,
        iterator,
        generator
    ]
    argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(6)
    ]
    str_argument_list = [
        f'([random.randint(0, 10**{n} - 1) for i in range(10**{n})], )'
        for n in range(6)
    ]

    def setup(function, argument):
        value_list = funcscale.repr_argument(argument)
        return '\n'.join((
            'from __main__ import ' + function.__name__,
            'from binary_search_tree import BinarySearchTree',
            'from binary_search_tree import BinarySearchNode',
            'bst = BinarySearchTree()',
            'for value in ' + value_list + ':',
            '   bst.insert(value)',
            'BinarySearchNode.__iter__ = ' + function.__name__
        ))

    def stmt(fucntion, argument):
        return '[value for value in bst]'

    # Set parameters.
    funcscale.function_list = function_list
    funcscale.argument_list = argument_list
    funcscale.str_argument_list = str_argument_list
    funcscale.stmt = stmt
    funcscale.setup = setup

    # Execute.
    funcscale.compare()


#
#
#
try:
    from binary_search_tree import Path
    from binary_search_tree import BinarySearchNode
except ModuleNotFoundError as err:
    print('%s: %s' % (err.__class__.__name__, str(err)))
    print('Please download binary_search_tree.py from ...')
    print('https://github.com/domodomodomo/binary_search_tree')
    import sys
    sys.exit()
else:
    from typing import Iterator


def list_iterator(
    binary_search_node: BinarySearchNode
) -> Iterator[BinarySearchNode]:
    return iter(binary_search_node.list())


def iterator(
    binary_search_node: BinarySearchNode
) -> Iterator[BinarySearchNode]:
    return Path(binary_search_node)


def generator(
    binary_search_node: BinarySearchNode
) -> Iterator[BinarySearchNode]:
    bsn = binary_search_node
    if bsn.left:
        yield from bsn.left
    yield bsn.value
    if bsn.right:
        yield from bsn.right


#
#
#
if __name__ == '__main__':
    comparison()
