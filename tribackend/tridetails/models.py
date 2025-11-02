from django.db import models


class Walkin(models.Model):
    croName = models.CharField(max_length=100)
    techStaff = models.CharField(max_length=100)
    counselingStaff = models.CharField(max_length=100)
    walkName = models.CharField(max_length=100)
    walkTime = models.TimeField()
    product = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.walkName} - {self.product}"

# registration
from django.db import models

class SheelaRegistration(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    enquire_product = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    staff_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=20, choices=[('single', 'Single'), ('installment', 'Installment')])
    installment_count = models.IntegerField(blank=True, null=True)
    installment_date = models.DateField(blank=True, null=True)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    otp_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# lead
from django.db import models

class Lead(models.Model):
    croName = models.CharField(max_length=100)
    leadName = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    reference = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.leadName

# app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = [
    ("super admin", "Super Admin"),
    ("admin", "Admin"),
    ("networkz systems", "Networkz Systems"),
    ("bdm", "BDM"),
    ("it desk", "IT Desk"),
]

class CustomUser(AbstractUser):
    # reuse username/email fields from AbstractUser
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default="admin")
    subRole = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"




from django.db import models

class Attendance(models.Model):
    TYPE_CHOICES = [
        ('Regular', 'Regular'),
        ('Weekend', 'Weekend'),
    ]
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    staff = models.CharField(max_length=100)
    date = models.DateField()
    student_name = models.CharField(max_length=100)
    timing = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    product = models.CharField(max_length=100)
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    module = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.type}"




from django.db import models

from django.db import models

class Activity(models.Model):
    ACTIVITY_MAX_LEN = 120

    activity_type = models.CharField(max_length=ACTIVITY_MAX_LEN)
    auto_no = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    phone_no = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=2)  # "01", "02" ... "12"
    # optional moderation field
    approved = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # ensure month is two-digit based on created_at if not provided
        if not self.month:
            self.month = ("0" + str(self.created_at.month)).slice(-2) if self.created_at else ""
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.activity_type} - {self.auto_no} - {self.created_at}"

# from django.db import models

class Seminar(models.Model):
    date = models.DateField()
    college = models.CharField(max_length=200)
    dept = models.CharField(max_length=100)
    resource = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    studentcount = models.PositiveIntegerField()
    feedback = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.college} - {self.resource} ({self.date})"







from django.db import models

class PendingService(models.Model):
    SERVICE_CHOICES = [
        ('internship', 'Internship'),
        ('workshop', 'Workshop'),
        ('course', 'Course'),
    ]

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    student_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    product_designation = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return f"{self.student_name} - {self.service_type}"