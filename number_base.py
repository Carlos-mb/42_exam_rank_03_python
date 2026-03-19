"""Create a function that receives a number in any base and returns the same
value in other base.
Bases are between 02 and 36
The chars are 0-9 A-Z"""

def convert_base(value, from_base, to_base):
    """
    Converts a string value from one base to another.
    Supports bases 2 through 36.
    """
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    # Step 1: Convert the input string to a decimal (Base 10) integer
    # Python's int() function handles up to base 36 automatically
    # I spent 30 minutes to do this manually:
    decimal_value = int(str(value), from_base)

    if decimal_value == 0:
        return "0"

    # Step 2: Convert the decimal integer to the target base
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = chars[remainder] + result
        decimal_value //= to_base

    return result
