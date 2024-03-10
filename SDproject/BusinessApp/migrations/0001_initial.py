# Generated by Django 4.2.5 on 2024-03-08 16:12

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(help_text='best size: 440x440px', upload_to='brand')),
                ('is_active', models.BooleanField(default=True, help_text="Check this for 'Active'")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=191)),
                ('profile_pic', models.ImageField(blank=True, upload_to='products_images/')),
                ('company_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('business_line', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(help_text='best size: 440x440px', upload_to='category')),
                ('is_active', models.BooleanField(default=True, help_text="Check this for 'Active'")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color_name', models.CharField(max_length=100, unique=True)),
                ('color_select', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, unique=True)),
                ('is_active', models.BooleanField(default=True, help_text="Check this for 'Active'")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('message', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Contact-Us',
                'verbose_name_plural': 'Contact-Us',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('tages', models.CharField(blank=True, max_length=200, null=True)),
                ('marked_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', tinymce.models.HTMLField()),
                ('specification', tinymce.models.HTMLField()),
                ('is_active', models.BooleanField(default=True, help_text="Check this for 'Active'")),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BusinessApp.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusinessApp.category')),
                ('color', models.ManyToManyField(blank=True, to='BusinessApp.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size_name', models.CharField(max_length=100)),
                ('size_detail', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text="Check this for 'Active'")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product')),
                ('is_active', models.BooleanField(default=True, help_text="Check this for 'Active'")),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='BusinessApp.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, to='BusinessApp.size'),
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('companyname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusinessApp.businessowner')),
            ],
        ),
    ]
