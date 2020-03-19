from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from companies.models import Company
from django.core.validators import MaxValueValidator, MinValueValidator

# Kudos default / reset value specified here
KUDOS_COUNT_DEFAULT = 3


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False)
    # Adding constraint of Kudos count's min and max values
    kudosCount = models.IntegerField(default=KUDOS_COUNT_DEFAULT, validators=[MaxValueValidator(KUDOS_COUNT_DEFAULT), MinValueValidator(0)])
    kudosLastUpdated = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.user.username
