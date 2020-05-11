def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    new_str = value.replace(" ", "")
    result = new_str.lower()
    return result == result[::-1]
