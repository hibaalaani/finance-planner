from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=(('Income', 'Income'), ('Expense', 'Expense')))


    def __str__(self):
        return f"{self.description} - {self.amount}"    
    
    
    
class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.monthly_limit}"    
    