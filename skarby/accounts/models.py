from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


def account_avatar_upload_to(instance, filename):
    """
    This method creates a new path for upload_to in Account model. Params instance and filename are identified in
    FileField class.
    :param instance: Class object. In this case instance is a class Account object.
    :param filename: Example filename.jpg.
    :return: New path for avatar upload_to.
    """
    # get account name through ForeignKey to Account. Same as Account.name
    account_name = instance.name
    return f"{account_name}/avatar/{filename}"


class Account(models.Model):
    name = models.CharField(max_length=70, verbose_name='Імя/Назва')
    description = models.TextField()
    instagram = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to=account_avatar_upload_to, verbose_name='Аватар')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def account_photos_upload_to(instance, filename):
    """
    This method creates a new path for upload_to in Photo model. Params instance and filename are identified in
    FileField class.
    :param instance: Class object. In this case instance is a class Photos object.
    :param filename: Example filename.jpg.
    :return: New path for photo upload_to.
    """
    # get account name through ForeignKey to Account. Same as Photos.accounts.name
    account_name = instance.accounts.name
    return f"{account_name}/account_photos/{filename}"


class Photos(models.Model):
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Аккаўнт')
    photo = models.ImageField(upload_to=account_photos_upload_to, verbose_name='Фота')

    def __str__(self):
        return self.photo.name
