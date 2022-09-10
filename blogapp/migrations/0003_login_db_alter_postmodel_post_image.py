# Generated by Django 4.0.4 on 2022-05-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_postmodel_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginuser', models.CharField(max_length=20)),
                ('loginpass', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='post_image',
            field=models.ImageField(null=True, upload_to='post_media/'),
        ),
    ]