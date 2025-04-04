# Write a function that takes an integer input and returns the sum of its digits.


def sum_of_digits(n):
    """
    This function takes an integer n and returns the sum of its digits.
    
    Parameters:
    n (int): The input integer (can be positive or negative).

    Returns:
    int: The sum of the digits of the absolute value of n.
    """
    # Convert the number to its absolute value to handle negative numbers
    n = abs(n)
    
    # Convert the number to a string, iterate over each character, convert it to an integer, and sum them
    return sum(int(digit) for digit in str(n))

# Example usage:
print(sum_of_digits(1234))  # Output: 10 (1 + 2 + 3 + 4)
print(sum_of_digits(-567))  # Output: 18 (5 + 6 + 7)

    