# Generated by Django 3.2.12 on 2022-11-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('OA', 'Organization Admin'), ('SA', 'Super Admin'), ('NU', 'Normal User')], default='NU', max_length=20),
        ),
    ]
