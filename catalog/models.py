from django.db import models
from django.urls import reverse
import uuid #for unique instances
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100, help_text="Input category (e.g. Home, Office)")

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True) #1 item = 1 owner, 1 owner = many items
	summary = models.TextField(max_length=1000, help_text='Input description of the item')
	category = models.ManyToManyField(Category)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('item-detail', args=[str(self.id)])

	def get_category(self):
		return ', '.join([category.name for category in self.category.all()[:3]])
	get_category.short_description = 'Category'

class Owner(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=50)

	class Meta:
		ordering = ["last_name","first_name"]

	def get_absolute_url(self):
		return reverse('owner-detail', args=[str(self.id)])

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)

class ItemInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True) 
	due_back = models.DateField(null=True, blank=True)
	loan_status = (('o', 'On loan'),('a', 'Available'),('r', 'Reserved'))
	status = models.CharField(max_length=1, choices=loan_status, blank=True, default='a')
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	
	class Meta:
		ordering = ["due_back"]
		permissions = (("can_mark_returned", "Set item as returned"),)

	def __str__(self):
		return '{0} ({1})'.format(self.id,self.item.name)

	@property #gets property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False