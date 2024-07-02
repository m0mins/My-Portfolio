from django.contrib import admin
from portfolioApp.models import User,Profile,Pricing,Skills,ProfessionalExperience,WorkSummary,Experience_Summary,EducationalHistory,AppDetails,App_Image,AppImages,FrequentQuestion
# Register your models here.
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import BaseInlineFormSet




class AppImageInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        
        # Check if at least one image is present
        if any(self.errors):
            return

        has_at_least_one_image = False

        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('app_img'):
                    has_at_least_one_image = True
                    break

        if not has_at_least_one_image:
            raise forms.ValidationError('At least one image is required.')

class Experience_SummaryInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Ensure that at least one size is selected
        if not any(form.cleaned_data.get('details') for form in self.forms):
            raise ValidationError('You must select at least one point of summary.')
class Product_SizeInline(admin.TabularInline):
    model = Experience_Summary
    formset = Experience_SummaryInlineFormSet
class ProductImageInline(admin.TabularInline):
    model = App_Image
    extra = 1
    formset = AppImageInlineFormSet

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Pricing)
admin.site.register(Skills)
admin.site.register(ProfessionalExperience)
admin.site.register(WorkSummary)
admin.site.register(Experience_Summary)
admin.site.register(EducationalHistory)
admin.site.register(AppDetails)
admin.site.register(App_Image)
admin.site.register(FrequentQuestion)

#admin.site.register(AppDetails,ProductAdmin)