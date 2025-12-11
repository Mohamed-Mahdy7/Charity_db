from django.db import models
import uuid
from projects.models import Project

# Create your models here.
class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField(null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    PAYMENT_METHODS = (
        ("card", "Credit Card"),
        ("paypal", "PayPal"),
        ("bank", "Bank Transfer"),
    )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="donations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"