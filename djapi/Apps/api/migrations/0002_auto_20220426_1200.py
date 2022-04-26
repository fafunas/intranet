# Generated by Django 3.2.5 on 2022-04-26 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'db_table': 'Forms',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('video', models.FileField(max_length=200, upload_to='training/')),
                ('created', models.DateTimeField(auto_now=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Training',
                'db_table': 'Training',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='update',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='update',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='training_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('training_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.training')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Training User',
                'verbose_name_plural': 'Training Users',
                'db_table': 'Training_User',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='training_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=200, verbose_name=django.db.models.fields.TextField)),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.forms')),
                ('training_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.training_user')),
            ],
            options={
                'verbose_name': 'Training Status',
                'verbose_name_plural': 'Training Status',
                'db_table': 'Training_Status',
                'ordering': ['id'],
            },
        ),
    ]