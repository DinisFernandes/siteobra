from django.db import models
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

# Create your models here.

class Tarefas(models.TextChoices):
    TE = 'TE', 'Terraplanagem'
    DR = 'DR', 'Drenagem'
    PA = 'PA', 'Pavimentação'
    OB = 'OB', 'Obras Acessórias'
    SI = 'SI', 'Sinalização e segurança'
    OA = 'OA', 'Obras de Arte'
    DI = 'DI', 'Diversos'

class Trocos(models.TextChoices):
    T1 = 'T1', 'Troço 1'
    T2 = 'T2', 'Troço 2'
    T3 = 'T3', 'Troço 3'


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Conteudo', blank=True, null=True)
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    trocos = models.CharField(max_length=2,
                                 choices= Trocos.choices,
                                 default= Trocos.T1,)
    location = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Pk', blank=True, null=True)
    latitude = models.DecimalField(max_digits=20,  decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20,  decimal_places=10, blank=True, null=True)
    tarefas = models.CharField(max_length=2,
                                 choices= Tarefas.choices,
                                 default= Tarefas.TE,)
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try :
            self.resize_image(self.imagem_post.name, 800)
        except:
            pass

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width <= new_width:
            img.close()
            return

        new_height = round(new_width * height / width)
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=60)
        new_image.close()

    def get_tarefa_name(self):
        return self.get_tarefas_display()

    def get_troco_name(self):
        return self.get_trocos_display()