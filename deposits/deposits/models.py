from django.db import models
from deposit_class import deposit as deposit_method


class Deposit(models.Model):
    deposit = models.DecimalField(decimal_places=2, max_digits=20)
    term = models.IntegerField()
    rate = models.DecimalField(decimal_places=2, max_digits=4)
    # interest = models.FloatField

    # def calculate_interest(self):
    #     interest = deposit_method(deposit=self.deposit, term=self.term, rate=self.rate)
    #     return interest


