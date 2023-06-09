from django.db import models

# Create your models here.

state_choice = (
	("Maharashtra", "Maharashtra"),
)
city_choice = (
	("Mumbai", "Mumbai"),
)



class Register(models.Model):
    username = models.TextField(max_length = 20)
    email = models.EmailField()
    password = models.TextField()
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    pincode = models.TextField()

    def __str__(self):
        return self.username



class Warehouse(models.Model):
    username = models.TextField(max_length = 20)
    warehousename  = models.TextField(max_length = 20)
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    pincode = models.IntegerField()
    lenght = models.IntegerField()
    bredth = models.IntegerField()
    height = models.IntegerField()
    area = models.IntegerField()
    images = models.ImageField(upload_to='images')
    date = models.DateField()
    # date=datetime.today()


    def __str__(self):
        return self.warehousename


class Good(models.Model):
    abc = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank = True, null = True)
    username = models.TextField(max_length = 20)
    warehousename  = models.TextField(max_length = 20, default = 0)  
    goodname  = models.TextField(max_length = 20)
    lenght = models.IntegerField()
    bredth = models.IntegerField()
    height = models.IntegerField()
    area = models.IntegerField()
    images = models.ImageField(upload_to='images')
    date = models.DateField()




    def __str__(self):
        return self.username + " " +self.goodname