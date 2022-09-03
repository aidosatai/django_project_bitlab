from django.db import models

class Category(models.Model):
    category_name = models.CharField('назваие категории', max_length=20, unique=True)

    def str(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    product_title = models.CharField('назваие продукта', max_length=20, unique=True)
    product_price = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def str(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
