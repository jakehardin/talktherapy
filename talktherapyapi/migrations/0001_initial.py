from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=250)),
                ('profile_image_url', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=50)),
                ('created_on', models.DateField()),
                ('active', models.BooleanField()),
                ('is_therapist', models.BooleanField()),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('created_on', models.DateField()),
                ('profile_image_url', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=500)),
                ('favorite', models.BooleanField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talktherapyapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField()),
                ('reviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talktherapyapi.user')),
                ('therapist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talktherapyapi.therapist')),
            ],
        ),
    ]
