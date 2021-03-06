# Generated by Django 3.2.4 on 2021-06-24 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BrandID', models.IntegerField(primary_key=True, serialize=False)),
                ('BrandName', models.CharField(max_length=40)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'Brand',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CartName', models.CharField(blank=True, max_length=40)),
                ('Description', models.TextField()),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Brand', to='CartApp.brand')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='CartApp.category')),
            ],
            options={
                'db_table': 'Cart',
                'managed': True,
            },
        ),
    ]
