from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class Review(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    rating = models.PositiveIntegerField(default=1)  # Rating from 1 to 5, for example
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Makes the Review model shared across tenants
        managed = True  # Allows it to be treated as a normal table
        db_table = "shared_review"  # Ensures a single table name for all tenants

    def __str__(self):
        return f"Review for {self.content_object} - Rating: {self.rating}"
