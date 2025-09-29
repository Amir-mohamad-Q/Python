def is_happy(n):
    seen_nums = set()
    while (n != 1) and (n not in seen_nums):
        seen_nums.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

is_happy(7)




if __name__ == '__main__':
    assert is_happy(7) is True
    assert is_happy(45) is False