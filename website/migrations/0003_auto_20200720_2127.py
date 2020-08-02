# Generated by Django 3.0.8 on 2020-07-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200720_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='Pk'),
        ),
    ]
