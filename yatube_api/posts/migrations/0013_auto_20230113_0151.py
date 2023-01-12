# Generated by Django 3.2.16 on 2023-01-12 22:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_auto_20230113_0150'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_subscribers',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]
