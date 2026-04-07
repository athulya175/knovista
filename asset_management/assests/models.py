from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Asset(models.Model):
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date_assigned = models.DateField()
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.asset}"

class InventoryItem(models.Model):
    item_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    threshold = models.PositiveIntegerField()

    def __str__(self):
        return self.item_type

class RepairTicket(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    issue = models.TextField()
    status = models.CharField(max_length=50)
    technician = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.asset} - {self.status}"
    