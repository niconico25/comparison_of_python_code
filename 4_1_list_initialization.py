import funcscale


def comparison():
    funcscale.function_list = [
        multicative_list,
        for_statement,
        for_statement_list_comprehension,
        while_statement,
        while_statement_with_iterator,
        while_statement_with_iterator_optimized,
    ]
    funcscale.argument_list = [
        ((10**i, ), {}) for i in range(4)
    ]
    return funcscale.compare()


#
#
#
def multicative_list(n):
    lst = [None] * n * n
    return lst


def for_statement(n):
    lst = []
    for i in range(n * n):
        lst.append(None)
    return lst


def for_statement_list_comprehension(n):
    lst = [None for i in range(n * n)]
    return lst


def while_statement(n):
    lst = []
    i = 0
    while i < n * n:
        lst.append(None)
        i += 1
    return lst


def while_statement_with_iterator(n):
    lst = []
    iterator = iter(range(n * n))
    while True:
        try:
            next(iterator)
        except StopIteration:
            break
        lst.append(None)
    return lst


def while_statement_with_iterator_optimized(n):
    lst = []
    iterator = iter(range(n * n))
    next_ = iterator.__next__
    append = lst.append
    while True:
        try:
            next_()
        except StopIteration:
            break
        append(None)
    return lst


#
#
#
if __name__ == '__main__':
    comparison()
