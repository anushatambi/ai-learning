def is_even_or_odd(number):
    """
    Checks if a number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: "even" if the number is even, "odd" if the number is odd.
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Examples
print(f"4 is {is_even_or_odd(4)}")  # Output: 4 is even
print(f"7 is {is_even_or_odd(7)}")  # Output: 7 is odd
print(f"0 is {is_even_or_odd(0)}")  # Output: 0 is even