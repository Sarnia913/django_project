# Generated by Django 4.0.5 on 2022-07-26 13:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a6e0cc26-136b-482c-b935-8dbd584caef4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]