def f(s=[]):
    """Return the length of s."""
    s.append(3)
    return len(s)

######### +++++++ Immutable Functions +++++++ ########


def square(x):
    """Return the square of x as an immutable function.
    >>> square(5)
    25
    >>> square(5)
    25
    """
    return x * x

######### +++++++ Mutable Functions +++++++ ########


def make_withdraw(balance):
    """Return a mutable balance"""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return balance
    return withdraw


def make_withdraw_list(balance):
    """Mutable values can be changed without a nonlocal statement. """
    b = [balance]

    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw
