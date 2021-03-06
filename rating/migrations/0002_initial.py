# Generated by Django 3.2.4 on 2021-06-30 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rating', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_mark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='mark',
            unique_together={('book', 'owner')},
        ),
    ]
