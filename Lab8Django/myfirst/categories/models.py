from django.db import models


class Category(models.Model):
    category_name = models.CharField('Название категории', max_length=200)

    def to_json(self):
        return {
            'category_name': self.category_name,
        }


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField('Название продукта', max_length=200)
    product_price = models.FloatField()
    product_description = models.TextField(default='')
    product_count = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'product_description': self.product_description,
            'product_count': self.product_count
        }
