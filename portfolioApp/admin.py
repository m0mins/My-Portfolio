from django.contrib import admin
from portfolioApp.models import User,Profile,Pricing,Skills,ProfessionalExperience,WorkSummary,Experience_Summary,EducationalHistory
# Register your models here.
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import BaseInlineFormSet

class Experience_SummaryInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Ensure that at least one size is selected
        if not any(form.cleaned_data.get('details') for form in self.forms):
            raise ValidationError('You must select at least one point of summary.')
class Product_SizeInline(admin.TabularInline):
    model = Experience_Summary
    formset = Experience_SummaryInlineFormSet
    
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Pricing)
admin.site.register(Skills)
admin.site.register(ProfessionalExperience)
admin.site.register(WorkSummary)
admin.site.register(Experience_Summary)
admin.site.register(EducationalHistory)