from django.contrib import admin
from .models import Hotel, Room, Guest, Booking


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "country", "phone_number", "email", "rating")
    search_fields = ("name", "city", "country")
    list_filter = ("city", "country", "rating")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "hotel",
        "room_number",
        "room_type",
        "price_per_night",
        "is_available",
    )
    search_fields = ("hotel__name", "room_number", "room_type")
    list_filter = ("hotel", "room_type", "is_available")


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number")
    search_fields = ("first_name", "last_name", "email", "phone_number")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "guest",
        "room",
        "check_in",
        "check_out",
        "total_price",
        "is_confirmed",
    )
    search_fields = ("guest__first_name", "guest__last_name", "room__room_number")
    list_filter = ("is_confirmed", "check_in", "check_out")
    date_hierarchy = "check_in"

    # Calculate total price before saving
    def save_model(self, request, obj, form, change):
        if not obj.total_price and obj.check_in and obj.check_out:
            nights = (obj.check_out - obj.check_in).days
            obj.total_price = nights * obj.room.price_per_night
        super().save_model(request, obj, form, change)
