import funcscale
import random


def comparison():
    funcscale.function_list = [
        for_statement_append,
        list_comprehension,
        while_statement,
        for_statement_del,
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**i - 1) for _ in range(10**i)], ), {})
        for i in range(6)
    ]
    funcscale.str_argument_list = [
        f'([random.randint(0, 10**i - 1) for _ in range(10**{i})], )'
        for i in range(6)
    ]
    return funcscale.compare()


#
#
#

# creating a new list.
def for_statement_append(lst):
    new_lst = []
    for e in lst:
        if e % 2 == 0:
            new_lst.append(e)
    return new_lst


def list_comprehension(lst):
    new_lst = [e for e in lst if e % 2 == 0]
    return new_lst


# deleting an element from an original list.
def while_statement(lst):
    tmp = []
    while lst:
        e = lst.pop()
        if e % 2 == 0:
            tmp.append(e)

    while tmp:
        lst.append(tmp.pop())

    return lst


def for_statement_del(lst):
    def reversed_enumerate(seq):
        return zip(reversed(range(len(seq))), reversed(seq))

    for i, e in reversed_enumerate(lst):
        if e % 2 == 1:
            del lst[i]
    return lst


#
#
#
if __name__ == '__main__':
    comparison()
