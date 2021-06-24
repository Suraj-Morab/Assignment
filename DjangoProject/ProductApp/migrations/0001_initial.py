# Generated by Django 3.2.4 on 2021-06-24 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CartApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ProductID', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(blank=True, max_length=40)),
                ('UnitPrice', models.DecimalField(decimal_places=4, max_digits=10)),
                ('description', models.TextField()),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartApp.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Products',
                'managed': True,
            },
        ),
    ]