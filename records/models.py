from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length=200)
	HKID = models.CharField(max_length=10)
	dateOfBirth = models.DateField()
	dateCaseConfirmed = models.DateField()
	caseNumber = models.PositiveIntegerField()
	def __str__(self):
	  return f'{self.name} {self.HKID} {self.dateOfBirth} {self.dateCaseConfirmed} {self.caseNumber}'

class Address(models.Model):
 	road = models.CharField(max_length=200)
 	district = models.CharField(max_length=200)
 	def __str__(self):
	  return f'{self.road} {self.district}'

class GridCoordinate(models.Model):
	xCoord = models.IntegerField()
	yCoord = models.IntegerField()
	def __str__(self):
	  return f'{self.xCoord} {self.yCoord}'

class DateBetween(models.Model):
	dateFrom = models.DateField()
	dateTo = models.DateField()
	def __str__(self):
	  return f'{self.dateFrom} {self.dateTo}'

class Category(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
	  return self.name

class Detail(models.Model):
	description = models.CharField(max_length=200)
	def __str__(self):
	  return self.description
	
class Location(models.Model):
	name = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	address = models.ManyToManyField(Address)
	gridcoordinate = models.ManyToManyField(GridCoordinate)
	datebetween = models.ManyToManyField(DateBetween)
	category = models.ManyToManyField(Category)
	detail = models.ManyToManyField(Detail)
	def __str__(self):
	  return self.name




