

class Deposit:

    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    def interest(self):
        _interest = 0
        total = int(self.deposit) * ((1 + float(self.rate)) ** int(self.term))
        _interest = total - self.deposit
        return _interest


deposit = Deposit(
    deposit=1000,
    term=2,
    rate=0.05,
)

interest = deposit.interest()
print(f"interest = {interest}")




