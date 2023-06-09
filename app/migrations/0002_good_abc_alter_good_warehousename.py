# Generated by Django 4.1.5 on 2023-04-19 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='abc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.warehouse'),
        ),
        migrations.AlterField(
            model_name='good',
            name='warehousename',
            field=models.TextField(default=0, max_length=20),
        ),
    ]