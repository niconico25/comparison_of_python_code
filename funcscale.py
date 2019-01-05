import timeit


#
# 1) arguments
#
function_list = None
argument_list = None


def setup(function, argument):
    """Return "from module import function"."""
    # 'argument' is pseudo parameter for override.
    return 'from __main__ import ' + function.__name__


def stmt(function, argument):
    """Return "function(*args, **kwargs)"."""
    return function.__name__ + repr_argument(argument)


#
# 2) main codes
#
def compare():
    """Compare execution times. Test if results are same for each argument."""
    _compare_result()
    _compare_time()


def _compare_result():
    """Test whether all results are same or not for each argument."""
    for argument in argument_list:
        result_generator = (_evaluate(function, argument)
                            for function in function_list)
        result_0 = next(result_generator)
        assert all(result_k == result_0 for result_k in result_generator),\
            'The results are not same.'


def _evaluate(function, argument):
    exec(setup(function, argument))
    return eval(stmt(function, argument))


def _compare_time():
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


"""Compare execution times among multiple functions and multiple parameters.

## 1. Example
### 1.1. Example code

        [4_3_sieve_of_eratosthenes.py](https://bit.ly/2Oh25bX)

Give a list of functions and a list of arguments, then
execute a funcscale.compare() function.

### 1.2. Example code

        [7_2_condition_exception.py](https://bit.ly/2DCJJhH)

If you want to change setup and stmt(parameters for timeit.timeit() function),
override funcscale.steup() function and funcscale.stmt() function.


## 2. Why does this code use global variables instead of arguments?

 * funcscale.function_list
 * funcscale.argument_list
 * funcscale.setup()
 * funcscale.stmt()


### 2.1. to avoid complexity
If we define API like below, the code would be complicated.
We should pass down the arguments for each functions.
```python
def compare(function_list, argument_list):
    _compare_result(function_list, argument_list)
    _compare_time(function_listm argument_list)
```

### 2.2. We don't have to worry about a side effect of this module.
funcscale.compare() function is expeted
to execute only one time for each script.

We never call the function, funcscale.compre(), two times or more in a script,
which means we don't have to consider
a side effect or a state of the module, funcscale.

So we can use global variables for this module.
"""
