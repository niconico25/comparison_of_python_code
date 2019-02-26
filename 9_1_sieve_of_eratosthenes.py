# https://python.ms/sub/algorithm/eratosthenes/
import funcscale
import collections


def comparison():
    funcscale.function_list = [
        primes,
        primes_fast,
        primes_dict,
        primes_ordered_dict
    ]
    funcscale.argument_list = [
        ((10**i, ), {}) for i in range(1, 5)
    ]
    funcscale.str_argument_list = [
        f'(10**{i}, )' for i in range(1, 5)
    ]
    funcscale.compare()


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def primes_fast(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def primes_ordered_dict(n):
    #
    prime_list = []
    non_prime_list = []
    number_dict = collections.OrderedDict(
        ((i, None) for i in range(n + 1)))
    #
    del number_dict[0]
    del number_dict[1]
    while True:
        # get prime
        prime, _ = number_dict.popitem(False)
        prime_list.append(prime)
        # break
        if prime * prime > n:
            break
        # get non primes
        non_prime_list.append(prime * prime)
        for k in number_dict:
            if prime * k <= n:
                non_prime_list.append(prime * k)
            else:
                break
        # delete non primes
        for non_prime in non_prime_list:
            del number_dict[non_prime]
        non_prime_list.clear()

    # add rest of numbers as prime
    prime_list.extend(
        [prime for prime, _ in number_dict.items()])

    return prime_list


def primes_dict(n):
    #
    prime_list = []
    non_prime_list = []
    k_list = []
    number_dict = {
        i: None for i in reversed(range(n + 1))}
    #
    del number_dict[0]
    del number_dict[1]
    while True:
        # get prime
        prime, _ = number_dict.popitem()
        prime_list.append(prime)
        if prime * prime > n:
            break

        # get non primes
        non_prime_list.append(prime * prime)
        while True:
            k, _ = number_dict.popitem()
            k_list.append(k)
            if prime * k > n:
                break
            non_prime_list.append(prime * k)

        while k_list:
            number_dict[k_list.pop()] = None

        # delete non prime
        while non_prime_list:
            del number_dict[non_prime_list.pop()]

    while number_dict:
        prime, _ = number_dict.popitem()
        prime_list.append(prime)

    return prime_list


if __name__ == '__main__':
    comparison()
