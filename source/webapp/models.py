from django.db import models

# Create your models here.

class GuestBook(models.Model):
    STATUS_CHOISES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано')
    ]
    author_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора')
    author_email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Почта автора')
    post_text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.TextField(max_length=100, null=False, blank=False, choices=STATUS_CHOISES, default='active', verbose_name='Статус')

    def __str__(self) -> str:
        return "{}. {} {} {}".format(self.pk, self.author_name, self.status, self.created_at)