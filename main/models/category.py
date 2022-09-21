from django.db import models

class Category(models.Model):
    category_name = models.CharField('назваие категории', max_length=20, unique=True)
    publish_date = models.DateTimeField(
        verbose_name='Дата публикации на сайте',
        auto_now_add=True,
        null=True,
        blank=True,
    )

    def str(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'