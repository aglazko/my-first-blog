from django.db import models
from django.utils import timezone

# Create your models here.
#определение модели, models.Model означает, что объект Post является моделью Django
class Post(models.Model):
	#models.ForeignKey — ссылка на другую модель
	author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
	#models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
	title=models.CharField(max_length=200)
	#models.TextField — так определяется поле для неограниченно длинного текста
	text=models.TextField()
	#models.DateTimeField — дата и время.
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

	#метод публикации для записи
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title