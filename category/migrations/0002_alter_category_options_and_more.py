# Generated by Django 4.0 on 2022-01-13 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_imge',
            new_name='category_image',
        ),
    ]