from decimal import Decimal, getcontext, ROUND_HALF_EVEN

def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using Binet's formula
    with high-precision decimal arithmetic.

    Args:
        n (int): Position in the Fibonacci sequence (0-based).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Set precision high enough to avoid rounding errors
    getcontext().prec = max(50, n + 10)

    sqrt5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt5) / Decimal(2)
    psi = (Decimal(1) - sqrt5) / Decimal(2)

    value = (phi ** n - psi ** n) / sqrt5
    return int(value.to_integral_value(rounding=ROUND_HALF_EVEN))


