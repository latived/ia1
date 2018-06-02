from django.db import models
from django.forms import ModelForm

# Create your models here.

# Expression = < Attribute, Operation, Value >
class Expression(models.Model):
    attribute = models.CharField(max_length=100)
    value = models.BooleanField()

    def __str__(self):
        return "%s = %s" % (self.attribute, self.value)

class Rule(models.Model):
    expressions = models.ManyToManyField(Expression,
            verbose_name="antecedents", symmetrical=False)
    consequent  = models.ForeignKey(Expression, on_delete=models.CASCADE,
            related_name='consequent')

    def __str__(self):
        exps = [str(exp) for exp in self.expressions.all()]
        return "IF " + " AND ".join(exps) + " THEN " + str(self.consequent)

class Fact(models.Model):
    expression = models.OneToOneField(Expression, on_delete=models.CASCADE,
            primary_key=True,
            )

    def __str__(self):
        return ' = '.join([self.expression.attribute,
            str(self.expression.value)])

