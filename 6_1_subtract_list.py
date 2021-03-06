import funcscale
import random


def comparison():
    funcscale.function_list = [
        subtract_list_try_remove,
        subtract_list_if_remove,
        subtract_list_for_if_del,
        subtract_list_while_if_pop,
    ]
    funcscale.argument_list = [
        (([i for i in range(0, 1000)], [i for i in range(0, 1000)]), {}),
        (([i for i in range(0, 1000)], [i for i in range(999, -1, -1)]), {}),
        (([i for i in range(0, 1000)], [i for i in range(1000, 2000)]), {}),
        (([random.randint(0, 1000) for _ in range(1000)],
          [random.randint(0, 1000) for _ in range(1000)]), {}),
    ]
    funcscale.str_argument_list = [
        '([i for i in range(0, 1000)], [i for i in range(0, 1000)])',
        '([i for i in range(0, 1000)], [i for i in range(999, -1, -1)])',
        '([i for i in range(0, 1000)], [i for i in range(1000, 2000)])',
        '([random.randint(0, 1000) for _ in range(1000)],'
        + '[random.randint(0, 1000) for _ in range(1000, 2000)])',
    ]
    funcscale.compare()


def subtract_list_try_remove(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        try:
            lst.remove(e2)
        except ValueError:
            continue
    return lst


def subtract_list_if_remove(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        if e2 in lst:
            lst.remove(e2)
    return lst


def subtract_list_for_if_del(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        for i, e1 in enumerate(lst):
            if e1 == e2:
                del lst[i]
                break
    return lst


def subtract_list_while_if_pop(lst1, lst2):
    lst = lst1.copy()
    lst.reverse()
    lst_c = []
    lst_pop = lst.pop
    lst_c_append = lst_c.append
    for e2 in lst2:
        while lst:
            e1 = lst_pop()
            if e1 == e2:
                break
            else:
                lst_c_append(e1)
        lst_c.reverse()
        lst.extend(lst_c)
        lst_c.clear()
    lst.reverse()
    return lst


if __name__ == '__main__':
    comparison()
