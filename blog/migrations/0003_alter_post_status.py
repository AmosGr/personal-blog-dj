# Generated by Django 5.0.6 on 2024-07-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_choise_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Rascunho'), (1, 'Publicar')], default=0),
        ),
    ]
