# Generated by Django 4.2.4 on 2023-10-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('interest', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='ocategory',
            field=models.CharField(choices=[('Abstract', 'Abstract'), ('Technology', 'Technology'), ('Digital', 'Digital')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='opurchasedate',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='oquantity',
            field=models.IntegerField(),
        ),
    ]