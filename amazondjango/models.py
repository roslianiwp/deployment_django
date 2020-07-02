from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    # profile_picture = models.ImageField(upload_to='')
    # address = models.CharField(max_length=255)
    # birthdate = models.DateField('Date of birth')
    # gender = models.CharField(choices=gender_list,max_length=1)
    # billing_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"

class ProductType(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"

class ProductTV(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=100)
    technologies = models.TextField(max_length=3000)
    desc_intro_title = models.CharField(max_length=255)
    desc_intro_det = models.CharField(max_length=255)
    desc_intro_pic = models.ImageField(upload_to='')
    button_carr_1 = models.CharField(max_length=100)
    button_carr_2 = models.CharField(max_length=100)
    
    price = models.IntegerField(default=0)
    connective_tech = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    back_light = models.CharField(max_length=255)
    hdr = models.CharField(max_length=255)
    viewing_angle = models.CharField(max_length=255)
    motion_rate = models.CharField(max_length=255)
    audio = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    # stock = models.IntegerField(default=0)
    # status = models.CharField(max_length=20)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class ProductPictureTV(models.Model):
    producttv = models.ForeignKey(ProductTV, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CarouselTV1(models.Model):
    producttv = models.ForeignKey(ProductTV, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CarouselTV2(models.Model):
    producttv = models.ForeignKey(ProductTV, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='')
    desc_spec_1 = models.CharField(max_length=100)
    desc_spec_2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class ProductShofa(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    desc_intro_title = models.CharField(max_length=255)
    desc_intro_det = models.CharField(max_length=255)
    desc_intro_pic = models.ImageField(upload_to='')
    detail = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=100)
    item_dimensions = models.CharField(max_length=255)
    material_type = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class ProductPictureShofa(models.Model):
    productshofa = models.ForeignKey(ProductShofa, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TotalRating(models.Model):
    total_rating = models.FloatField(default=0)
    
class ProductReview(models.Model):
    product = models.ForeignKey(ProductTV, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null = True, blank = True)
    total_rating = models.FloatField(default=0)
    customer_rating = models.FloatField(default=0)
    customer_review = models.TextField(max_length=1000)
    customer_picture = models.ImageField(upload_to='', default='sofa-1-1_AsDOsaD.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"review product {self.product}"
    
