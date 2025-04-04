# Write a Python function factorial(n) that calculates the factorial of a non-negative integer n 
# using recursion. Additionally, ensure that the function raises a ValueError if the input n is not 
# a non-negative integer.

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.
    Raises ValueError if n is not a non-negative integer.
    """
    if not isinstance(n,int) or n<0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n==1:
        return 1
    else:
      return n * factorial(n - 1)