from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name="Название")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="news/%Y/%m/%d/",
                              blank=True, null=True,  verbose_name="Фоновое-Изображение")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата Создания")
    updatedAt = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Our_team(models.Model):
    title = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name="Имя")
    position = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name="Должность")
    description = models.TextField(
        null=True, blank=True, verbose_name="Характеристика")
    image = models.ImageField(upload_to="news/%Y/%m/%d/",
                              blank=True, null=True,  verbose_name="Фоновое-Изображение")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата Создания")
    updatedAt = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша исполнительная команда"