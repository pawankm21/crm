# Generated by Django 3.1.1 on 2020-11-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20201127_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('prime', 'prime'), ('new', 'new')], max_length=200, null=True),
        ),
    ]