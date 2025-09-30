def add(x: int | float, y: int | float) -> int | float:
    """Returns the sum of x and y."""
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    """Returns the difference of x and y."""
    return x - y


def multiply(x: int | float, y: int | float) -> int | float:
    """Returns the product of x and y."""
    return x * y


def divide(x: int | float, y: int | float) -> int | float | None:
    """Returns the quotient of x and y."""
    if y == 0:
        return None
    return x / y


def power(x: int | float, y: int | float) -> int | float:
    """Returns x raised to the power of y."""
    return x ** y
