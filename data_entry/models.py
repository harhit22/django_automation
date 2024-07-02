from django.db import models


class Student(models.Model):
    roll_no = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=128)
    age = models.IntegerField(null=False, blank=False, default=18)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)

    def __str__(self):
        return self.customer_name


class Empolyee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=128)
    desgination = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    retirement = models.DecimalField(max_digits=10, decimal_places=2)
    other_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_compenstation = models.DecimalField(max_digits=10, decimal_places=2)
