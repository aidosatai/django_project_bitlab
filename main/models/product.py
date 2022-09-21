from django.db import models

class Product(models.Model):
    product_title = models.CharField('назваие продукта', max_length=20, unique=True)
    product_price = models.IntegerField(default=0)
    # product_category = models.ForeignKey(Product, on_delete=models.CASCADE)

    def str(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
