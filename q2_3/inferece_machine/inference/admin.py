from django.contrib import admin

from .models import Rule, Fact, Expression

# Register your models here.

admin.site.register(Rule)
admin.site.register(Fact)
admin.site.register(Expression)
