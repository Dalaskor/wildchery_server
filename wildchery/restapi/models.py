from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(max_length=30, null=True)
    phone_number = models.IntegerField(null=True)
    is_seller = models.BooleanField(default=False)
    profile_image = models.ImageField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.price} Р."


class ProductPhoto(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photo')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')


class Review(models.Model):
    description = models.TextField()
    rating = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')


class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery')



class DeliveryProduct(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='delivery_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='delivery_product')


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')


class FavoritesProduct(models.Model):
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, related_name='favorites_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites_product')

