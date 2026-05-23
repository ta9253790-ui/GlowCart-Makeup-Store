from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class Order(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=200)

    price = models.IntegerField()

    quantity = models.IntegerField()

    image = models.ImageField(upload_to='orders/')

    status = models.CharField(max_length=100, default="Order Placed")

    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.product_name
    
class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name