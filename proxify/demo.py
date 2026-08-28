# Given an array A of N integers, find the smallest positive integer
# (greater than 0) that does not occur in A.


def solution(A: list[int]) -> int:
    A.sort()
    former_positive = 0
    for element in A:
        if element <= 0:
            continue
        if former_positive == element:
            continue
        if former_positive == element - 1:
            former_positive = element
            continue
        return former_positive + 1
    return former_positive + 1


if __name__ == "__main__":
    print(solution([13, -1, 0, 1, 2, 4, 5, -5]))
