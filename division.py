def division(num1: int, num2: int) -> Tuple[int, int]:
    """Perform integer division using successive subtraction.

    Arguments:
        num1 (int): The number to be divided.
        num2 (int): The number to divide by.

    Returns:
        Tuple[int, int]: A tuple containing (quotient, remainder).
    """
    if num2 == 0:
        print("Error: division by zero")
        return 0,0

    quotient: int = 0
    remainder: int = num1

    while remainder >= num2:
        remainder -= num2
        quotient += 1

    return quotient, remainder



