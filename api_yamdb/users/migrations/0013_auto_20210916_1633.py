# Generated by Django 2.2.16 on 2021-09-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210914_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Confirmation',
        ),
    ]