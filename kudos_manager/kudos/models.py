from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Kudo(models.Model):
    fromColleague = models.ForeignKey(
        User, related_name='fromColleage', on_delete=models.CASCADE)
    toColleague = models.ForeignKey(
        User, related_name='toColleague', on_delete=models.CASCADE)
    message = models.CharField(
        max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        if self.fromColleague == self.toColleague:
            raise Exception('An employee attempted to send kudos to himself/herself')
        super(Kudo, self).save(*args, **kwargs)