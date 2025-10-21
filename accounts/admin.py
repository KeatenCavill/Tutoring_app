from django.contrib import admin
from .models import TutorProfile


# Register your models here.
@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "subject",
        "mon_start",
        "mon_end",
        "tue_start",
        "tue_end",
        "wed_start",
        "wed_end",
        "thur_start",
        "thur_end",
        "fri_start",
        "fri_end",
    )
    search_fields = ("user__username", "user__first_name", "user__last_name", "subject")
    list_filter = ("subject",)
