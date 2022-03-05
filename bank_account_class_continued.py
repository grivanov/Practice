class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        
    # Write your code here
        self._balance = 0.0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, number):
        if type(number) in [int, float] and number >= 0 and number <= 100000:
            self._balance = number
        else:
            return
