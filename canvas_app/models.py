from django.db import models

class LoginProfessor(models.Model):
    email = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 100)
