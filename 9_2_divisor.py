import funcscale
from typing import List


def comparison():
    funcscale.function_list = [
        _divisorize_pair,
        _divisorize_syntax,
        _divisorize_naive,
    ]
    funcscale.argument_list = [
        ((2**2 * 3**2 * 5**2, ), {}),
        ((2**2 * 3**3 * 5**3, ), {}),
        ((2**2 * 3**3 * 5**4, ), {}),
        ((3313**2 * 3323**3, ), {}),
        ((3313**3 * 3323**4, ), {}),
        ((3313**3 * 3323**5, ), {}),
    ]
    funcscale.str_argument_list = [
        '(2**2 * 3**2 * 5**2,)',
        '(2**2 * 3**3 * 5**3,)',
        '(2**2 * 3**3 * 5**4,)',
        '(3313**2 * 3323**3,)',
        '(3313**3 * 3323**4,)',
        '(3313**3 * 3323**5,)',
    ]
    funcscale.compare()


# unify function's input and output interface for funcscale.
def _divisorize_pair(n: int) -> List[int]:
    return sorted([num_pair(div)
                  for div in divisorize_pair(factorize_pair(n))])


def _divisorize_syntax(n: int) -> List[int]:
    return sorted([num_pair(div)
                  for div in divisorize_syntax(factorize_pair(n))])


def _divisorize_naive(n: int) -> List[int]:
    return sorted([num_naive(div)
                  for div in divisorize_naive(factorize_naive(n))])


#
# pair
#
def divisorize_pair(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize_pair(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def factorize_pair(n):
    # 素数と仲良しになる3つのプログラム - ぴよぴよ.py
    # http://cocodrips.hateblo.jp/entry/2014/02/02/011119
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def num_pair(fct):
    n = 1
    for base, exponent in fct:
        n = n * base**exponent
    return n


#
# syntax
#
def divisorize_syntax(fct):
    div = []
    if not fct:
        div.append([])
        return div
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize_syntax(fct)
    suf_div = [[(b, k)] for k in range(e + 1)]
    for pre in pre_div:
        for suf in suf_div:
            div.append(pre + suf)
    return div


#
# naive
#
def divisorize_naive(fct):
    # bit list
    bit_len = len(fct)
    r = range
    bit_list = [[(i >> j) % 2 for j in r(bit_len)] for i in r(2**bit_len)]
    # divisor
    div = [[f for f, b in zip(fct, bit) if b] for bit in bit_list]
    div[0] = [1]
    #   exclude duplication, such as  [2, 2, 0], [2, 0, 2], [0, 2, 2].
    div = [list(t) for t in set([tuple(d) for d in div])]
    return div


def factorize_naive(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct


def num_naive(fct):
    n = 1
    for e in fct:
        n = n * e
    return n


#
# main
#
if __name__ == '__main__':
    comparison()
