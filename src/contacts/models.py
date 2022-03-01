from django.db import models

# Create your models here.
class BackCall(models.Model):

    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Номер телефона", max_length=25)
    data_added = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Обратный звонок и вопрос"
        verbose_name_plural = "Обратные звонки и вопросы"