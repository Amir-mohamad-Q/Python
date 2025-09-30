from constansts import ABOVE_100, UNDER_20, TENs


def num_to_word(num: int)-> str:
    """
    Convert a number to its worl representation.

    :param num: the number of convert.
    :return: The world representation of the number.

    >>> num_to_word(0)
    'Zero'
    >>> num_to_word(123)
    'One Hundred Twenty Three'
    """
    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        reminder = num % 10
        if reminder == 0:
            return f"{TENs[num // 10]}"
        return f"{TENs[num // 10]}  {UNDER_20[reminder]}"
    
    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    return f"{p1} {p2} {num_to_word(num % pivot) if num % pivot != 0 else ''}"

print(num_to_word(123))