from django.db import models

class Salesperson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Mechanic (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Car(models.Model):
    serial_number = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    year = models.IntegerField()
    for_sale = models.BooleanField(default=True)
    
    def __str__(self):
        return self.make + " " + self.model
    
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.IntegerField()
    
    def __str__(self):
        return self.service_name
    
class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.invoice_number
    
class ServiceTicket(models.Model):
    ticket_number = models.CharField(max_length=100)
    date_received = models.DateField()
    date_returned = models.DateField(null=True, blank=True)
    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    comments = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.ticket_number
    
class Parts(models.Model):
    
    part_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    purchase_price = models.IntegerField()
    retail_price = models.IntegerField()
    
    def __str__(self):
        return self.part_number
    
class PartsUsed(models.Model):
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    
    number_used = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.part.part_number
    
class ServiceMechanic(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    
    hours = models.IntegerField()
    rate = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return str(self.mechanic)
