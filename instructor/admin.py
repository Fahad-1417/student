from django.contrib import admin
from .models import InstructorProfile
from .models import ProfessionalCourse

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')
    search_fields = ('user__username', 'specialty')



admin.site.register(ProfessionalCourse)
