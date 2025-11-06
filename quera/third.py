# function takes an integer (n), if we have a square and draw n parallel lins to the sides of the square, 
# return the number of maximum number of regions the square is divided into.
# def max_regions(n):
#     return (n * (n + 1)) // 2 + 1

# print(max_regions(1))
# print(max_regions(2))
# print(max_regions(3))
# print(max_regions(4))
# print(max_regions(5))
# print(max_regions(6))
# print(max_regions(7))
# print(max_regions(8))

def max_regions(n: int) -> int:
    """
    Return the maximum number of regions a square is divided into
    when n straight lines are drawn, each line being parallel to one
    of the square's sides (i.e., horizontal or vertical).
    n must be a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return ((n // 2) + 1) * (((n + 1) // 2) + 1)
    # alternatively: return ( (n + 2)**2 ) // 4

input_n = int(input())
print(max_regions(input_n))
# print(max_regions(1))
# print(max_regions(2))
# print(max_regions(3))
# print(max_regions(4))
# print(max_regions(5))
# print(max_regions(6))
# print(max_regions(7))
# print(max_regions(8))