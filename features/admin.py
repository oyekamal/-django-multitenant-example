# feature/admin.py

from django.contrib import admin
from .models import Feature, Bro  # , TestModel

# Register the Feature model
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "hotel", "is_active")
    search_fields = ("name", "hotel")
    list_filter = ("is_active",)


# Register the Bro model
@admin.register(Bro)
class BroAdmin(admin.ModelAdmin):
    list_display = ("name",)


# # Register the TestModel
# @admin.register(TestModel)
# class TestModelAdmin(admin.ModelAdmin):
#     list_display = ('name', )
#     search_fields = ('name',)
