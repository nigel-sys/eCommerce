# Generated by Django 2.1.15 on 2022-12-07 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_auto_20221207_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProductTimestamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='TTime Stamp')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timestamps', to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timestamps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]