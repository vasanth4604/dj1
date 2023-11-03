from django.db import models

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length = 100)
	aemail = models.EmailField()
	category = models.CharField(max_length = 50)
	def str(self):
		return self.name
class Customer(models.Model):
	name = models.CharField(max_length=100)
	aemail = models.EmailField()
	category = models.CharField(max_length=50)

class Order(models.Model):
	oid = models.CharField(max_length=30)
	oname = models.CharField(max_length=30)
	odescription = models.CharField(max_length=30)
	oprice = models.FloatField(max_length=30)
	oquantity = models.IntegerField()
	obill = models.FloatField(max_length=30)
	opurchasedate = models.DateField(max_length=30)
	CAT_CHOICES = (('Abstract', 'Abstract'), ('Technology', 'Technology'),('Digital', 'Digital'),)
	ocategory = models.CharField(max_length=20, choices=CAT_CHOICES)

class Person(models.Model):
	name = models.CharField(max_length=100)
	age = models.CharField(max_length=100)
	country = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	interest = models.CharField(max_length = 20)
