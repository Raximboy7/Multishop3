# Generated by Django 4.1.6 on 2023-06-23 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=30)),
                ('size', models.CharField(choices=[('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44')], max_length=100)),
                ('how', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('map', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myhome.product')),
            ],
        ),
    ]
