def digits_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


def solution(n: int) -> int:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, digits_sum(a) + digits_sum(b)
    return a if n == 0 else b


if __name__ == "__main__":
    assert digits_sum(13) == 4
    assert digits_sum(12) == 3
    assert digits_sum(8) == 8

    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(7) == 13
    assert solution(8) == 12
    assert solution(9) == 7
    assert solution(10) == 10
    assert solution(11) == 8
