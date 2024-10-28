from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("content_object", "rating", "comment", "created_at", "updated_at")
    search_fields = ("comment", "content_type__model")
    list_filter = ("rating", "created_at")
    date_hierarchy = "created_at"
