from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=70, verbose_name='Імя/Назва')
    description = models.TextField()
    instagram = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Аватар')


class Photos(models.Model):
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Аккаўнт')
    photo = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Фота')

