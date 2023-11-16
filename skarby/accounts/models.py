from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

class Account(models.Model):
    name = models.CharField(max_length=70, verbose_name='Імя/Назва')
    description = models.TextField()
    instagram = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Аватар')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Photos(models.Model):
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Аккаўнт')
    photo = models.ImageField(upload_to='media/photos/%Y/%m/%d/', verbose_name='Фота')

    def __str__(self):
        return self.photo.name
