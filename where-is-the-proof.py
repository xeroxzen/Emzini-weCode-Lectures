# Polymorphic functions
# implementing __repr__ and __str__

class Dog:
    """A Dog"""

    def __init__(self):
        self.__repr__ = lambda: 'drogon'
        self.__str__ = lambda: 'drogon the dog'

    def __repr__(self):
        return 'Dog()' 

    def __str__(self):
        return 'a dog'
