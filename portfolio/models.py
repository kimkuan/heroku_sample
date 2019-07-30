from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    # 업로드된 이미지들을 images 폴더 안에 넣어라!
    image = models.ImageField(upload_to = 'images/', default='https://image.flaticon.com/icons/svg/149/149852.svg')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
