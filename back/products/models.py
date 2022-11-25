from PIL import Image
from django.core.files import File
from io import BytesIO
from django.db import models


class Category(models.Model):
    name = models.CharField('Category Name', max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField('Product Name', max_length=255)
    equipment = models.TextField()
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    image1 = models.ImageField(upload_to='products/%Y/%m/%d')
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)

    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.category.name} {self.name}'

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image1(self):
        if self.image1:
            return 'http://127.0.0.1:8000' + self.image1.url
        return ''

    def get_image2(self):
        if self.image2:
            return 'http://127.0.0.1:8000' + self.image2.url
        return ''

    def get_image3(self):
        if self.image3:
            return 'http://127.0.0.1:8000' + self.image3.url
        return ''

    def get_image4(self):
        if self.image4:
            return 'http://127.0.0.1:8000' + self.image4.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url

        if self.image1:
            self.thumbnail = self.make_thumbnail(self.image1)
            self.save()

            return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail



