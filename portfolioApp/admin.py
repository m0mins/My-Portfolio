from django.contrib import admin
from portfolioApp.models import User,Profile,Pricing,Skills,ProfessionalExperience,WorkSummary
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Pricing)
admin.site.register(Skills)
admin.site.register(ProfessionalExperience)
admin.site.register(WorkSummary)