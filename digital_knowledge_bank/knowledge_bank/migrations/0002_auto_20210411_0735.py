# Generated by Django 2.2 on 2021-04-11 07:35

from django.conf import settings
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('knowledge_bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField()),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='knowledge_bank.Tag')),
            ],
        ),
    ]
