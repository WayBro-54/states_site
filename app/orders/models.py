from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Orders(models.Model):
    symbol = models.CharField(max_length=10)
    open_data = models.DateTimeField(verbose_name='Дата открытия ордера')
    close_data = models.DateTimeField(verbose_name='Дата закрытия ордера')
    open_price = models.CharField(25, verbose_name='Цена открытия')
    close_price = models.CharField(25, verbose_name='Цена закрытия')
    user = models.ForeignKey(User,
                             related_name='order',
                             on_delete=models.PROTECT,
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'История оредров'
        verbose_name_plural = 'История ордеров'

    def __str__(self):
        return f'{self.user}, {self.symbol}'
    

class OrderSettings(models.Model):
    min_diff = models.FloatField(verbose_name='Минимальная раздвжка')
    user = models.ForeignKey(User,
                             related_name='order_settings',
                             on_delete=models.PROTECT,
                             verbose_name='Пользователь')
    volume = models.FloatField(verbose_name='Общий объем')
    volume_orders = models.FloatField(verbose_name='Объем на одну сделку')
    stopls = models.FloatField(verbose_name='Стоп лосс в долларах')
    teykpr = models.FloatField(verbose_name='Тейк профит в долларах')

    class Meta:
        verbose_name = 'Настройки ордеров'
        verbose_name_plural = 'Настройки ордеров'
    