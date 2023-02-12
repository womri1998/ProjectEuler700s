from functools import cache
from modulo import modulo


million = 10 ** 6


@cache
def two_pals(n: int, length: int, contains_2: bool) -> modulo:
    if n < length:
        return modulo(0, million)
    if length < 3:
        return modulo(int(contains_2 or length * 2 == n), million)
    if length % 2 == 1:
        # implies that contains_2 == False
        return sum(two_pals(n - i, length - 1, i == 2) for i in range(1, n))
    else:
        if n % 2 == 1:
            return modulo(0, million)
        return sum(two_pals(n - 2 * i, length - 2, contains_2 or i == 2) for i in range(1, n))


def t(n: int) -> int:
    return sum(two_pals(n, i, False) for i in range(1, n + 1)) % million


def main():
    print(t(6))
    print(t(42))
    n = 43
    while t(n) % 1000000 != 0:
        n += 1
        if n % 10 == 0:
            print(n)
    print(n)


if __name__ == '__main__':
    main()
