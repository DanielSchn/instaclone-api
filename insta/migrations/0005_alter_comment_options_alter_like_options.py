# Generated by Django 5.1.1 on 2024-09-12 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['created_at']},
        ),
    ]
