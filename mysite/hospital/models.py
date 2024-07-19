from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50, unique=True)
    licence_number = models.DateField()
    years_of_experience = models.PositiveSmallIntegerField()
    education = models.CharField(max_length=26, unique=True)
    hospital = models.CharField(max_length=26, unique=True)

    def __str__(self):
        return self.user


class MedicalRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.doctor}"


class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.reason}'


class Medication(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=26)
    dosage = models.TextField()

    def __str__(self):
        return self.name


class FitnessProgram(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=26)
    description = models.TextField()

    def __str__(self):
        return self.user


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.message}"
