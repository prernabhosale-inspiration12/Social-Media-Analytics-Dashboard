from django.db import models
from django.contrib.auth.models import User
from departments.models import Department


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    phone = models.CharField(max_length=15, blank=True)

    designation = models.CharField(max_length=100)

    joining_date = models.DateField()

    def __str__(self):
        return self.user.username