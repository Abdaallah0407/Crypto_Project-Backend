from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="news/%Y/%m/%d/",  verbose_name="Фоновое-Изображение")
    createdAt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата Создания")
    updatedAt = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменение")

    def __str__(self):
        return self.title

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url=''
    #     return url

    # @property
    # def image_url(self):
    #     """
    #     Return self.photo.url if self.photo is not None,
    #     'url' exist and has a value, else, return None.
    #     """
    #     if self.image:
    #         return getattr(self.photo, 'url', None)
    #     return None
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    # @property
    # def get_photo_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return ''

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
