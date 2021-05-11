from django.shortcuts import render

from django.views.generic import (FormView, ListView, DetailView,)
from deposits.forms import AddDepositForm
from deposit_class import deposit
from deposits import (
    forms,
    models,
)


class AddDepositView(FormView):
    template_name = "add_deposit.html"
    form_class = AddDepositForm
    success_url = "deposit/new"

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form=form)
        return response


class ListOfDeposits(ListView):
    model = models.Deposit


class DepositeDetailView(DetailView):
    model = models.Deposit
    template_name = "deposit_detail.html"

