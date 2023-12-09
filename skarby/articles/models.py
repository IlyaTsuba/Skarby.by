from django.db import models
from accounts.models import Account
from users.models import CustomUser


class ArticleCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Назва катэгорыі')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Катэгорыя"
        verbose_name_plural = "Катэгорыі"
        ordering = ['id']


class Article(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Чарнавік',
        PUBLISHED = 1, 'Апублікавана'

    title = models.CharField(max_length=150, verbose_name='Загаловак')
    content = models.TextField(verbose_name='Тэкст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час стварэння')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='Катэгорыя')
    account = models.ManyToManyField(Account, blank=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Артыкул"
        verbose_name_plural = "Артыкулы"
        ordering = ['id']


class ArticleLikes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


def article_photos_upload_to(instance, filename):
    """
    This method creates a new path for upload_to in Account model. Params instance and filename are identified in
    FileField class.
    :param instance: Class object. In this case instance is a class Article object.
    :param filename: Example filename.jpg.
    :return: New path for photo upload_to.
    """
    # get account name through ForeignKey to Article. Same as Article.name
    article_title = instance.article.title
    return f"articles/{article_title}/photos/{filename}"


class ArticlePhotos(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_photos',
                                verbose_name='Артыкул')
    photo = models.ImageField(upload_to=article_photos_upload_to, verbose_name='Фота')

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Фота'
        verbose_name_plural = 'Фота'
