# Generated by Django 3.2.7 on 2021-12-11 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0004_auto_20211211_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bens',
            name='id_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bens', to='patrimonio.marcas'),
        ),
    ]