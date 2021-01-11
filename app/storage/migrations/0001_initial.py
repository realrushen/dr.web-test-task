# Generated by Django 3.1.5 on 2021-01-10 19:52

from django.db import migrations, models
import storage.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_name', models.CharField(blank=True, editable=False, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=storage.utils.custom_path_handler)),
                ('hash', models.CharField(blank=True, max_length=255, unique=True)),
                ('directory', models.CharField(blank=True, editable=False, max_length=2)),
            ],
        ),
    ]
