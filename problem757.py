def stealthy_count(limit: int) -> int:
    stealthies = set()
    i = 1
    while i * (i + 1) <= limit:
        j = 1
        stealthy = i * (i + 1) * j * (j + 1)
        while j <= i and stealthy <= limit:
            stealthies.add(stealthy)
            j += 1
            stealthy = i * (i + 1) * j * (j + 1)
        i += 1
    return len(stealthies)


if __name__ == "__main__":
    print(stealthy_count(10 ** 14))
