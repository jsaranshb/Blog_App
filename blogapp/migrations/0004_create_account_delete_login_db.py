# Generated by Django 4.0.4 on 2022-05-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_login_db_alter_postmodel_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(max_length=10)),
                ('user_name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='login_db',
        ),
    ]