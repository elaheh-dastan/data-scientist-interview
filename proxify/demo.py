# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()
    former_positive = 0
    for element in A:
        if element <= 0:
            continue
        if former_positive == element:
            continue
        if former_positive == (element - 1):
            former_positive = element
            continue
        return former_positive + 1
    return former_positive + 1




instance = solution([13, -1, 0,1, 2,4,5, -5])
print(instance)