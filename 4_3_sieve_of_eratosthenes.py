import funcscale


def comparison():
    funcscale.function_list = [
        primes_for,
        primes_while,
    ]
    funcscale.argument_list = [
        ((10**i, ), {}) for i in range(7)
    ]
    funcscale.str_argument_list = [
        f'(10**{i}, )' for i in range(7)
    ]
    funcscale.compare()


#
#
#
def primes_for(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def primes_while(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    i = 2
    while i <= n:
        j = i + i
        while j <= n:
            is_prime[j] = False
            j += i
        i += 1
    return [i for i in range(n + 1) if is_prime[i]]


#
#
#
if __name__ == '__main__':
    comparison()
