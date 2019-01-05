import funcscale
import random
try:
    import binary_search_tree
except ModuleNotFoundError as err:
    print('%s: %s' % (err.__class__.__name__, str(err)))
    print('Please download binary_search_tree.py from ...')
    print('https://github.com/domodomodomo/binary_search_tree')
    import sys
    sys.exit()


def comparison():
    # Create parameters.
    function_list = [
        binary_search_tree.list_iterator,
        binary_search_tree.iterator,
        binary_search_tree.generator
    ]
    argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(6)
    ]

    def setup(function, argument):
        value_list = funcscale.repr_argument(argument)
        return '\n'.join((
            'from binary_search_tree import BinarySearchTree',
            'from binary_search_tree import BinarySearchNode',
            'from binary_search_tree import ' + function.__name__,
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
    funcscale.stmt = stmt
    funcscale.setup = setup

    # Execute.
    funcscale.compare()


if __name__ == '__main__':
    comparison()
