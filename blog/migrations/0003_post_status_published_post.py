# Generated by Django 4.2.4 on 2023-09-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_date_alter_post_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status_published_post',
            field=models.BooleanField(default=False),
        ),
    ]
