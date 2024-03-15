from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', null=True, blank=True)
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='опубликовано')
    number_of_views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.content}'

    class Meta:
        verbose_name = 'название блога'
        verbose_name_plural = 'названия блогов'
