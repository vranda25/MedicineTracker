from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# import sys
# sys.path.insert(1, '\MedicineTracker\medicineTracker\accounts\models.py')
#
# import CustomUser

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True, null=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    blood_group = models.CharField(max_length=20, blank=True, null=True)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    heart_rate = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(editable=False, default="0000-03-29T04:56:49.782685Z")
    modified = models.DateTimeField(default="0000-03-29T04:56:49.782685Z")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user.email)


class Allergies(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name_of_allergy = models.CharField(max_length=50, default='-')
    reaction = models.CharField(max_length=500, default='-')

    def __str__(self):
        return str(self.user.email)+' : '+str(self.name_of_allergy)


class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name_of_disease = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField( blank=True, null=True)
    end_date = models.DateField( blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.user.email)+' : '+str(self.name_of_disease)


