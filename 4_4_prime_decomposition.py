import funcscale
import itertools


def comparison():
    funcscale.function_list = [
        prime_decomposition_for,
        prime_decomposition_for_itertools,
        prime_decomposition_while,
    ]
    funcscale.argument_list = [
        ((2**3 * 3**12 * 5**7, ), {}),
        ((3313**3 * 3323**3, ), {}),
        ((9973**5 * 9932**3 * 9901**2, ), {}),
        ((9973**5 * 9932**3 * 9901**2, ), {}),
        ((111869**3 * 128461**2, ), {}),
        ((111869**3 * 128461**2 * 188459**3, ), {}),
    ]
    funcscale.str_argument_list = [
        '(2**3 * 3**12 * 5**7, )',
        '(3313**3 * 3323**3, )',
        '(9973**5 * 9932**3 * 9901**2, )',
        '(9973**5 * 9932**3 * 9901**2, )',
        '(111869**3 * 128461**2, )',
        '(111869**3 * 128461**2 * 188459**3, )',
    ]
    return funcscale.compare()


#
#
#
def prime_decomposition_for(n):
    table = []
    for i in range(2, n):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            table.append(i)
    if n > 1:
        table.append(n)
    return table


def prime_decomposition_for_itertools(n):
    table = []
    for i in itertools.count(2, 1):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            table.append(i)
    if n > 1:
        table.append(n)
    return table


def prime_decomposition_while(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


#
#
#
if __name__ == '__main__':
    comparison()
