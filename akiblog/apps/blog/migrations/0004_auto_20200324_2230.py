# Generated by Django 3.0.3 on 2020-03-24 19:30

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коммент', 'verbose_name_plural': 'Комменты'},
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='article_title'),
        ),
    ]
