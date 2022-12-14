# Generated by Django 4.1.1 on 2022-09-21 02:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, upload_to='documentation/images/')),
                ('url', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('manual_order', models.IntegerField(default=1)),
                ('icon', models.CharField(blank=True, max_length=55)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, upload_to='documentation/images/')),
                ('url', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('slug', models.CharField(default='', max_length=55)),
                ('sub_title', models.CharField(blank=True, max_length=55)),
                ('topic_level', models.IntegerField(choices=[(1, 'Nivel I'), (2, 'Nivel II'), (3, 'Nivel III')], default=1)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('framework', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='languages.framework')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
            ],
            options={
                'ordering': ['topic_level'],
                'unique_together': {('title', 'language', 'framework')},
            },
        ),
    ]
