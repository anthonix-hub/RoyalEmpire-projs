# Generated by Django 2.1.8 on 2022-02-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Royalemp_commerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, null='True'),
        ),
    ]