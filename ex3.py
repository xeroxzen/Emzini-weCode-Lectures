# Let's have a look at classes
class Clown:
    """An illustration of a class statement. This class is not useful

    >>> Clown.nose
    'big and red'
    >>> Clown.dance()
    'No thanks'
    """

    nose = 'big and red'

    def dance():
        return 'No thanks'


class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('Eric')
    >>> a.holder
    'Eric'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount('Andile')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


class Bank:
    """A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> andile = bank.open_account('Andile', 10)
    >>> zola = bank.open_account('Nokuzola', 5, CheckingAccount)
    >>> zola.interest
    0.01
    >>> andile.interest = 0.06
    >>> bank.pay_interest()
    >>> andile.balance
    10.6
    >>> zola.balance
    5.05
    """

    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, account_type=Account):
        """Open an account_type for holder and deposit amount."""

        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self): 
        """Pay interest to all accounts."""
        for account in self.accounts:
            account.deposit(account.balance * account.interest)
