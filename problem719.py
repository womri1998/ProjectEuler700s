def recursive_s(n: int, index: int, total: int) -> bool:
    square_str = str(n ** 2)
    if total > n:
        return False
    if index == len(square_str):
        return total == n
    if total + int(square_str[index:]) < n:
        return False
    return any((recursive_s(n, i + 1, total + int(square_str[index: i + 1]))
                for i in range(index, min(index + len(str(n)) + 1, len(square_str)))))


def s_number(n: int) -> bool:
    if n % 10000 == 0:
        print(n)
    return recursive_s(n, 0, 0)


def t(n: int) -> int:
    return sum((i ** 2 for i in range(2, n + 1) if s_number(i)))


if __name__ == "__main__":
    print(t(10 ** 6))
