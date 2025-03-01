from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.user.username
    
# Create a User Profile by default when a user register an account
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user= instance)
        user_profile.save()

# Automate the create profile thing
post_save.connect(create_profile, sender=User)




# Categories of shoes
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

# Customers
class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.name} , {self.surname}"


# Producys 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    size = models.IntegerField(default=4)
    category = models.ManyToManyField(Category)
    small_description = models.CharField(max_length=100000, default='', blank=True, null=True)
    description = models.CharField(max_length=100000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/') 
    image1 = models.ImageField(upload_to='uploads/product/' , blank=True)
    image3 = models.ImageField(upload_to='uploads/product/' , blank=True)
    image4 = models.ImageField(upload_to='uploads/product/' , blank=True)
    image5 = models.ImageField(upload_to='uploads/product/', blank=True )
    image6 = models.ImageField(upload_to='uploads/product/' , blank=True)
    image7 = models.ImageField(upload_to='uploads/product/' , blank=True)
    image8 = models.ImageField(upload_to='uploads/product/' , blank=True)

    # add On Sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    best_seller = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})


class Order(models.Model):
   
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.product