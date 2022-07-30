"""
All the calculations assume that k divides n.
Any parameter named "ones" is the number of ones inside a single k-window
The solution works for only for even k, n.
"""
from math import comb, factorial
from modulo import mod, modulo


M = 10 ** 9 + 7


def given_columns_with_order(k: int, n: int, ones: int) -> int:
    return 2 ** (ones * n // k)


def given_columns_without_order(k: int, n: int, ones: int) -> int:
    zeroes = (k - ones) // 2
    one_orderings = comb(k, ones)
    zeroes_orderings = comb(zeroes * 2, zeroes)
    return one_orderings * zeroes_orderings * given_columns_with_order(k, n, ones)


def bad_a(k: int, n: int) -> int:
    return sum((given_columns_without_order(k, n, 2 * i + k % 2) for i in range(k // 2 + 1)))


def factorial_mod(n: int, m: int) -> modulo:
    result = mod(1, m)
    for i in range(1, n + 1):
        result *= i
    return result


def choose_mod(n: int, k: int, m: int) -> modulo:
    return factorial_mod(n, m) * (factorial_mod(k, m) * factorial_mod(n - k, m)) ** -1


def a(k: int, n: int) -> int:
    one_orderings = mod(1, M)
    zero_orderings = choose_mod(k, k // 2, M)
    column_orderings = mod(1, M)
    column_orderings_factor = mod(2, M) ** (2 * mod(n // k, M))
    total = mod(0, M)
    for i in range(k // 2):
        total += one_orderings * zero_orderings * column_orderings
        one_orderings *= mod((i + 1) * (i + 2), M) ** -1  # * mod((n - i) * (n - i - 1), M)
        zero_orderings *= mod(k // 2 - i - 1, M) ** 2  # * mod((n - i) * (n - i - 1), M) ** -1
        column_orderings *= column_orderings_factor
    total += one_orderings * zero_orderings * column_orderings
    return total.residue


if __name__ == "__main__":
    # print(bad_a(3, 9))
    # print(bad_a(4, 20))
    print(a(4, 20))

