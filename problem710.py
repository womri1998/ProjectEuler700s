from modulo import mod, modulo


M = 10 ** 6


def center_twopals(n: int) -> int:
    return (mod(2, M) ** ((n - 2) // 2 - 1)).residue


if __name__ == "__main__":
    print(center_twopals(6))
    print(center_twopals(20))
    print(center_twopals(42))
