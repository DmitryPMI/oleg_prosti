# Generated by Django 2.1.2 on 2018-10-21 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181021_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=4096)),
                ('post_date', models.DateTimeField(verbose_name='the date on which the post will be sent')),
            ],
        ),
        migrations.CreateModel(
            name='IntroQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegramId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.TelegramUser')),
            ],
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='RegularEvents',
        ),
        migrations.DeleteModel(
            name='UserAnketa',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.IntroQuestion'),
        ),
    ]