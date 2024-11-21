from django.db import models
'''class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    publication_date=models.DateField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    def is_expensive(self):
        return self.price>50'''
    
'''class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=100)
    is_enrolled=models.BooleanField()
    
    def is_passing(self):
        return self.grade>'C'''

'''class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()

    def calculate_total_cost(self):
        return self.price*self.quantity'''

'''class Order(models.Model):
    order_number=models.CharField(max_length=200)
    customer_name=models.CharField(max_length=200)
    order_date=models.DateField()
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)

    def is_high_value(self):
        return self.total_amount>1000'''
    
class Product_Details(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return self.name


    
    