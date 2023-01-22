# Author: Google Jr
# Generalizing patterns using arguments and Higher Order Functions

def split(n):
    """
    Splits a positive integer into all but its last digit
    """
    return n // 10, n % 10

def sum_digits(n):
    """
    Return the sum of the digits of positive integer n. """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    """
    Return the digit sum of N computed by the Luhn Algorithm.
    """

    '''
    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100)
    20
    >>> luhn_sum(4012888888881881)
    90
    >>> luhn_sum(6048451000195665)
    60
    >>> luhn_sum(8926301000872750)
    60
    '''

    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    """
    Return the Luhn sum of N by doubling the last digit.
    """

    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)

    if n < 10:
        return luhn_digit
    return luhn_sum(all_but_last) + luhn_digit


if __name__ == "__main__":
    import doctest
    doctest.testmod()