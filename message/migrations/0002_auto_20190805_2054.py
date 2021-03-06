# Generated by Django 2.2.3 on 2019-08-05 11:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('message', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Recipient'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
        ),
    ]
