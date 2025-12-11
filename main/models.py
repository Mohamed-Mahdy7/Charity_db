from django.db import models
from django.contrib.auth import get_user_model
from donations.models import Donation
import uuid

User = get_user_model()

# Create your models here.
class PaymentLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name="payment_logs")
    raw_payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class AdminLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action


class SystemSettings(models.Model):
    id = models.AutoField(primary_key=True)
    site_name_ar = models.CharField(max_length=255)
    site_name_en = models.CharField(max_length=255)
    about_ar = models.TextField()
    about_en = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    social_links = models.JSONField(default=dict)

    def __str__(self):
        return self.site_name_en


