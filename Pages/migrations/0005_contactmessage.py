# Generated by Django 4.1.1 on 2023-04-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_alter_teammember_fb_alter_teammember_instangram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
