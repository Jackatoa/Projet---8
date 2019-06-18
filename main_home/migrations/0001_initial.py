# Generated by Django 2.2.2 on 2019-06-17 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aliment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('url_img', models.TextField()),
                ('url_nutri', models.TextField()),
                ('category', models.TextField()),
                ('stores', models.TextField()),
                ('nutriscore', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='AlimentSaved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('urloriginal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='originals', to='main_home.Aliment')),
                ('urlsubstitute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='substituted', to='main_home.Aliment')),
            ],
        ),
    ]
