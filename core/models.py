from django.db import models
from users.models import Account

import string
import random

# Create your models here.
class Venue(models.Model):
	def venue_num_generator(size=10, chars=string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	owner = models.ForeignKey(Account, on_delete=models.CASCADE)
	venue_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	# state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
	zipcode = models.CharField(max_length=5)
	venue_num = models.CharField(
		max_length = 10,
		blank=True,
		editable=False,
		unique=True,
		default=venue_num_generator(),
		)

	def __str__(self):
		return f"{self.venue_name}"

class CustomerLocation(models.Model):
	VENUE_CHOICES = tuple([(venue.venue_name,venue.venue_name) for venue in Venue.objects.all()])
	customer = models.ForeignKey(Account, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, choices=VENUE_CHOICES)

	def __str__(self):
		return f"{self.customer.first_name} is a customer at {self.location}"