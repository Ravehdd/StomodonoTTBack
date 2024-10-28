from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=255)


class Doctor(models.Model):
    name = models.CharField(max_length=255)


class UserData(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    personal_account = models.IntegerField()
    family_account = models.IntegerField()


class Patient(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    add_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True)
    cancel_time = models.DateTimeField(null=True)
    days_count = models.IntegerField(null=True)
    # card_comment = models.CharField(null=True, max_length=255)
    # reception_comment = models.CharField(null=True, max_length=255)


class AuthUsers(models.Model):
    patient = models.ForeignKey(UserData, on_delete=models.CASCADE)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

