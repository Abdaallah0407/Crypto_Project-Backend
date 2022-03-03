from django.db import models


class News(models.Model):
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

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"