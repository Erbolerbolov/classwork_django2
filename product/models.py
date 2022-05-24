from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(primary_key=True, max_length=150, verbose_name='слаг!')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='название продукта')
    desc = models.TextField(max_length=500, verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='product', verbose_name='категория')

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title



