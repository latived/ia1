from django.shortcuts import render
from django.views import generic

from .models import Rule, Fact

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'inference/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['rules_base'] = Rule.objects.all()
        context_data['facts_base'] = Fact.objects.all()
        return context_data


# Forward chaining: show what new facts we have given a rules' base with a facts
    # base
# Backward chaining: try to prove a question given a rules' base and a facts
    # base
class ProofMethods:
    def backward(goals, rules, facts):
        # ...
        return backward(antecedents, rules, facts)

    def forward(goal, rules, facts, pos=0):
        # ...
        return forward(goal, rules, facts, pos+1)

