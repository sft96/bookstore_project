from django.db import models

from users.models import CustomUser


class BookGenre(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название жанра')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название книги')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                verbose_name='Цена')
    author = models.CharField(max_length=50, verbose_name='Автор')
    image = models.ImageField(upload_to='book.images', null=True,
                              blank=True, verbose_name='Изображение')
    genre = models.ForeignKey(to=BookGenre, on_delete=models.CASCADE,
                              verbose_name='Жанр')

    class Meta:
        ordering = ['name']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'Книга: {self.name}, категория: {self.genre}'


class Basket(models.Model):
    quantity = models.SmallIntegerField(default=0,
                                        verbose_name='Количество товара')
    generated_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Когда товар был добавлен в корзину'
    )
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE,
                             verbose_name='Книга')

    class Meta:
        ordering = ['-generated_timestamp']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина с {self.book} для {self.user}'

    def sum(self):
        return self.book.price * self.quantity
