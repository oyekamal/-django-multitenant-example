from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True
    )  # e.g., 4.5

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
        ("deluxe", "Deluxe"),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    description = models.TextField(blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    booking_date = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} for {self.guest}"

    def save(self, *args, **kwargs):
        # Automatically calculate total price based on number of nights
        if not self.total_price and self.check_in and self.check_out:
            nights = (self.check_out - self.check_in).days
            self.total_price = nights * self.room.price_per_night
        super().save(*args, **kwargs)
