from django.db import models
from src.accounts.models import User
from src.products.models import Table_Product


class Sale(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username}"
        else:
            return f"{self.id}"

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи Пользователя"


class SaleItem(models.Model):
    product = models.ForeignKey(
        Table_Product, on_delete=models.CASCADE, blank=True, null=True)
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, blank=True, null=True, related_name="items")
    data_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Продажа в Базе"
        verbose_name_plural = "Продажи в Базе"

    def __str__(self):
        return f"{self.product.title}(id_{self.product.id})"
