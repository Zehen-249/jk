# Generated by Django 5.0.4 on 2024-05-02 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_posts_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='postName',
            new_name='poemName',
        ),
    ]
