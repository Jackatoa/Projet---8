# Generated by Django 2.2.2 on 2019-06-18 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliment',
            name='nutriscore',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='alimentsaved',
            name='urloriginal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originals', to='main_home.Aliment'),
        ),
        migrations.AlterField(
            model_name='alimentsaved',
            name='urlsubstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substituted', to='main_home.Aliment'),
        ),
    ]
