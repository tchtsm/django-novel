from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=20)
    user = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    intro = models.CharField(max_length=500)
    status = models.CharField(max_length=2)
    score = models.FloatField(max_length=3)

    class Meta:
        db_table = "book"