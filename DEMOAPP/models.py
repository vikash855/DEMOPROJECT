from django.db import models


class RegisterData(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "register_data"





