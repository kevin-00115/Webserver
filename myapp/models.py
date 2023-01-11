from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=200)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


