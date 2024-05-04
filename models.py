from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address} {self.create_at}'


class Goods(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    create_at = models.DateField(auto_now_add=True)

    def total_price(self):
        return self.price * self.amount

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.amount} {self.create_at}'


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    price = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client_id} {self.goods_id} {self.price} {self.create_at}'
