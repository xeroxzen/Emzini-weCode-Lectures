"""inheritance and Attribute lookup"""


class A:
    z = -1

    def f(self, x):
        return B(x - 1)


class B(A):
    n = 4

    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)


class C(B):
    def f(self, x):
        return x


a = A()
b = B(1)
b.n = 5


def plus_minus(x):
    yield x
    yield - x


def double(x):
    print('***', x, '=>', 2 * x, '***')
    return 2 * x


def a_then_b_for_loop(a, b):
    """Return the elements of A followed by those of B."""
    for x in a:
        yield x
    for x in b:
        yield x

# A simpler way as from python 3.3


def a_then_b(a, b):
    """Return the elements of A followed by those of B."""
    yield from a
    yield from b


def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


class Countdown:
    """Count down to zero from undefined x."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        v = self.start
        while v > 0:
            yield v
            v -= 1


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)


def prefixes(s):
    """yields all the prefixes of s."""
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    """Yields all the substrings of s. """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
