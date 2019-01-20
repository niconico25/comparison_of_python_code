"""比較用に書きました.

local スコープを使わず global スコープを使うと
ひたすら引数を関数に渡す作業が続く。

global スコープを使った書いたコードと比較するために、
新規に追加した引数は改行しました。
"""
import timeit


#
# 1) arguments
#
def _setup(function, argument):
    """Return "from module import function"."""
    # 'argument' is pseudo parameter for override.
    return 'from __main__ import ' + function.__name__


def _stmt(function, argument):
    """Return "function(*args, **kwargs)"."""
    return function.__name__ + repr_argument(argument)


#
# 2) main codes
#
def compare(
    function_list,
    argument_list,
    setup=_setup,
    stmt=_stmt
):
    """Compare execution times. Test if results are same for each argument."""
    _compare_result(function_list, argument_list,
        setup,
        stmt
    )
    _compare_time(function_list, argument_list,
        setup,
        stmt
    )


def _compare_result(
    function_list,
    argument_list,
    setup,
    stmt
):
    """Test whether all results are same or not for each argument."""
    for argument in argument_list:
        result_generator = (_evaluate(function, argument)
                            for function in function_list)
        result_0 = next(result_generator)
        assert all(result_k == result_0 for result_k in result_generator),\
            'The results are not same.'


def _evaluate(function, argument,
    setup,
    stmt
):
    exec(setup(function, argument))
    return eval(stmt(function, argument))


def _compare_time(function_list, argument_list,
    setup,
    stmt
):
    for argument in argument_list:
        print('#')
        for function in function_list:
            time = timeit.timeit(
                stmt=stmt(function, argument),
                setup=setup(function, argument),
                number=10)
            print(function.__name__.ljust(40), ':', "{0:7.4f}".format(time))


#
# 3) utility
#
def repr_argument(argument) -> str:
    """Return "(*args, **kwargs)"."""
    args, kwargs = argument
    args = ', '.join('%s' % a for a in args)
    kwargs = ', '.join('%s=%s' % (p, a) for p, a in kwargs.items())
    joint = ', ' if args and kwargs else ''
    return f'({args}{joint}{kwargs})'
