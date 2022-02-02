from itertools import count
from pyexpat import model
from django.db import models
from decimal import Decimal, MAX_PREC

# Create your models here.


class Table_Product(models.Model):
    title = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name="Название")

    count = models.FloatField(null=True, blank=True,
                              verbose_name="Количевство в месяц")
    totality = models.FloatField(
        null=True, blank=True, verbose_name='Совокупность в месяц')
    price = models.IntegerField(blank=True, verbose_name='Цена')
    price_device = models.IntegerField(
        null=True, blank=True, verbose_name='Доступно за 1 апарат')
    price_per_quantity = models.IntegerField(
        null=True, blank=True, verbose_name='Доступная цена за количевство апаратов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт в таблице"
        verbose_name_plural = "Продукт в таблице"


class CartItem(models.Model):
    product = models.ForeignKey(
        Table_Product, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(
        verbose_name="Цена", max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name="Количество", blank=True, null=True)

    data_added = models.DateTimeField(auto_now_add=True, null=True)



    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def __str__(self):
        return f"{self.product.title}"

    def get_cost(self):
        return self.price * self.quantity


class Table_Headers(models.Model):
    title = models.CharField(max_length=50, verbose_name="Загаловок")

    class Meta:
        verbose_name = "Загаловоки строк в таблицах"
        verbose_name_plural = "Загаловоки строк в таблицах"

    def __str__(self):
        return self.title
