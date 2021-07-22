# Generated by Django 2.2 on 2021-07-04 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imgfield_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='exp_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_number', models.IntegerField()),
                ('status', models.CharField(max_length=27)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products_in_quote', models.ManyToManyField(related_name='quotes_of_product', to='imgfield_app.Product')),
                ('quoted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quotes', to='imgfield_app.User')),
            ],
        ),
    ]
