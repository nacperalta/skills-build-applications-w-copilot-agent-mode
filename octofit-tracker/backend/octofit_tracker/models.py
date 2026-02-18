from django.db import models

# Placeholder models for OctoFit Tracker


class Activity(models.Model):
    name = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.name
