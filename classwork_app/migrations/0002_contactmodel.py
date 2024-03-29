# Generated by Django 2.1.7 on 2019-10-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classwork_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full name')),
                ('phone', models.CharField(max_length=11, verbose_name='Your Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Company Email')),
                ('referer', models.CharField(blank=True, choices=[('facebook', 'Faceboo'), ('instagram', 'Instagram'), ('nairaland', 'Nairaland'), ('twitter', 'Twitter'), ('', '')], default='', max_length=10)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=7)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('message', models.TextField()),
            ],
        ),
    ]
