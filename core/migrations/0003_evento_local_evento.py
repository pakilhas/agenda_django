# Generated by Django 4.1.7 on 2023-02-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.TextField(blank=True, null=True),
        ),
    ]
