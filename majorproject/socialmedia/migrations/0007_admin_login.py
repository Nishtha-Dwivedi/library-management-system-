# Generated by Django 4.0.4 on 2022-06-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0006_library_authorname_library_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]