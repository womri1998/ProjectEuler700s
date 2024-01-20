from math import ceil, log10, comb
from fractions import Fraction


DIGITS_COUNT = 3
M = 10 ** 16


def get_digits(n):
    return [(n // (10 ** i)) % 10 for i in range(ceil(log10(n)) + 1)]


def is_ds(n):
    digits = get_digits(n)
    return 2 * max(digits) == sum(digits)


def orderings(n, k_list):
    print(n, k_list)
    amount = 1
    for k in k_list:
        amount *= comb(n, k)
        n -= k
    return amount


def average_digit_value(digits, digits_count):
    return int(Fraction(sum(digits), digits_count) * sum([10 ** i for i in range(digits_count)]))

def viable_digits(total, max_count, max_digit = 9, digits: list = []):
    if total == 0:
        return [digits]
    elif max_digit == 0 or len(digits) >= max_count:
        return []
    viables = []
    for digit in range(min([total, max_digit]) + 1):
        new_digits = digits.copy()
        new_digits.append(digit)
        viables += viable_digits(total - digit, max_count, digit, new_digits)
    return viables


def digits_arrangements_sum(digits):
    x = average_digit_value(digits, DIGITS_COUNT) * orderings(DIGITS_COUNT, digits)
    print(x, digits)
    return x


def ds_sum(digits_count):
    total = 0
    for i in range(2, 10):
        for digits in viable_digits(i, DIGITS_COUNT):
            print("digits: " + str(digits + [i]))
            total += digits_arrangements_sum(digits + [i])
    return sum([digits_arrangements_sum(digits)]) % M

print([viable_digits(i, DIGITS_COUNT) for i in range(1, 10)])
print(ds_sum(DIGITS_COUNT))
# print(sum([x for x in range(2, 10 ** DIGITS_COUNT) if is_ds(x)]) % M)
