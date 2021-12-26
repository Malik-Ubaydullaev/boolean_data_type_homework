from math import sqrt
def main(a):
    result = sqrt(a)
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return result % 1 == 0