# function takes an integer (n), if we have a square and draw n parallel lines to the sides of the square,
# return the maximum number of regions the square is divided into.
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


if __name__ == "__main__":
    print(max_regions(int(input())))
