import funcscale


def comparison():
    funcscale.function_list = [
        for_statement,
        for_statement_speed_up,
        for_statement_list_comprehension,
    ]
    funcscale.argument_list = [
        ((i, ), {}) for i in range(7)
    ]
    funcscale.str_argument_list = [
        f'({i}, )' for i in range(7)
    ]
    return funcscale.compare()


def for_statement(i):
    random = linear_congruential_generators(48271, 8, 0, 2**31 - 1)
    lst = []
    for _ in range(10**i):
        lst.append(random())
    return lst


def for_statement_speed_up(i):
    random = linear_congruential_generators(48271, 8, 0, 2**31 - 1)
    lst = []
    append = lst.append
    for _ in range(10**i):
        append(random())
    return lst


def for_statement_list_comprehension(i):
    random = linear_congruential_generators(48271, 8, 0, 2**31 - 1)
    return [random() for _ in range(10**i)]


def linear_congruential_generators(a, x, b, m):
    def random():
        nonlocal x
        x = (a * x + b) % m
        return x
    return random


if __name__ == '__main__':
    comparison()
