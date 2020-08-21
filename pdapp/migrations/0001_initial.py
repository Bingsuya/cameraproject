# Generated by Django 3.1 on 2020-08-20 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmb', models.CharField(max_length=200, null=True)),
                ('digitalb', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LensType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdname', models.CharField(max_length=100, null=True)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('pic', models.ImageField(null=True, upload_to='%Y/%m/%d')),
                ('stars', models.IntegerField(null=True)),
                ('pdsale', models.IntegerField(null=True)),
                ('countbuy', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdtype', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(null=True)),
                ('pdname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdapp.product')),
                ('pdtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pdapp.type')),
            ],
            options={
                'ordering': ['-star'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='pdtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pdapp.type'),
        ),
    ]
