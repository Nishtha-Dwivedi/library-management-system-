# Generated by Django 4.0.4 on 2022-06-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0004_rename_name_student_sname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.CharField(max_length=10)),
                ('bookName', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]