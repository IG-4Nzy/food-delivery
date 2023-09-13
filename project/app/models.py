from django.db import models

class Person(models.Model):
    uname = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = 'custom_person_table'