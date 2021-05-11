from django import forms
from deposits import models
from deposit_class import Deposit


class AddDepositForm(forms.ModelForm):
    class Meta:
        model = models.Deposit
        fields = [
            "deposit",
            "term",
            "rate",
        ]

    def save(self, commit=True):
        deposit = super().save(commit=False)
        deposit.deposit = self.cleaned_data["deposit"]
        deposit.term = self.cleaned_data["term"]
        deposit.rate = self.cleaned_data["rate"]
        # deposit.interest = Deposit.interest(deposit=deposit.deposit, term=deposit.term, rate=deposit.rate)

        if commit:
            deposit.save()

        return deposit

