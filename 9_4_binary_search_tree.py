import funcscale
import random


def comparison():
    # Create parameters.
    function_list = [
        list_iterator,
        generator_iterator,
        original_iterator,
        original_iterator_parental,
    ]
    argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(6)
    ]
    str_argument_list = [
        f'[randint(0, 10**{n} - 1) for i in range(10**{n})]'
        for n in range(6)
    ]

    def setup(function, argument):
        value_list = funcscale.repr_argument(argument)
        path = 'tree.tree.binary_search_tree'
        return '\n'.join((
            'from __main__ import ' + function.__name__,
            'from ' + path + '               import BinarySearchTree',
            'from ' + path + '.parental      import BinarySearchNode',
            'bst = BinarySearchTree(BinarySearchNode)',
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
    from tree.tree.binary_search_tree.sequencial import Iterator as Sequencial
    from tree.tree.binary_search_tree.parental import Iterator as Parental
except ModuleNotFoundError as err:
    print('%s: %s' % (err.__class__.__name__, str(err)))
    print('Please download...')
    print('$ git clone https://github.com/niconico25/tree')
    import sys
    sys.exit()


def list_iterator(binary_search_node):
    return iter(binary_search_node.list())


def generator_iterator(binary_search_node):
    bsn = binary_search_node
    if bsn.left:
        yield from bsn.left
    yield bsn.value
    if bsn.right:
        yield from bsn.right


def original_iterator(binary_search_node):
    return Sequencial(binary_search_node)


def original_iterator_parental(binary_search_node):
    return Parental(binary_search_node)


#
#
#
if __name__ == '__main__':
    comparison()
