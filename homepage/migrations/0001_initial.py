# Generated by Django 5.1.3 on 2024-12-11 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_class', models.CharField(max_length=1000)),
                ('count_value', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'About Count',
                'verbose_name_plural': 'About Counts',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='AboutUsHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default='About Us', max_length=100)),
                ('title', models.CharField(default='Your Trusted Service Partner', max_length=200)),
            ],
            options={
                'verbose_name': 'About Us Header',
                'verbose_name_plural': 'About Us Header',
            },
        ),
        migrations.CreateModel(
            name='ContactHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default="Let's Connect", max_length=100)),
                ('title', models.CharField(default='Get in Touch', max_length=200)),
                ('description', models.TextField(default="Let's create something amazing together", max_length=300)),
            ],
            options={
                'verbose_name': 'Contact Section Header',
                'verbose_name_plural': 'Contact Section Header',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('site_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Contact Information',
            },
        ),
        migrations.CreateModel(
            name='EmailRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Email Recipient',
                'verbose_name_plural': 'Email Recipients',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='HeroSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_highlight', models.CharField(help_text='Text with gradient effect', max_length=100)),
                ('title_main', models.CharField(help_text='Main title text', max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('description_highlight', models.CharField(help_text='Highlighted text in description', max_length=200)),
                ('image', models.ImageField(upload_to='hero_slides/')),
                ('button_text', models.CharField(default='Book Our Services', max_length=50)),
                ('button_url', models.CharField(default='#contact', max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Hero Slide',
                'verbose_name_plural': 'Hero Slides',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logos/')),
                ('alt_text', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Logo',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='services/')),
                ('button_text', models.CharField(default='Book Us', max_length=50)),
                ('button_url', models.CharField(default='#contact', max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ServiceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default='Our Services', max_length=100)),
                ('title', models.CharField(default='Professional Solutions', max_length=200)),
            ],
            options={
                'verbose_name': 'Service Section Header',
                'verbose_name_plural': 'Service Section Header',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('icon', models.ImageField(upload_to='social_icons/')),
            ],
            options={
                'verbose_name_plural': 'Social Media Links',
            },
        ),
        migrations.CreateModel(
            name='TeamHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default='Our Team', max_length=100)),
                ('title', models.CharField(default='Meet Our Expert Team', max_length=200)),
            ],
            options={
                'verbose_name': 'Team Section Header',
                'verbose_name_plural': 'Team Section Header',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team/')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='WhyChooseFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('icon_class', models.ImageField(upload_to='whychooseus/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Why Choose Us Feature',
                'verbose_name_plural': 'Why Choose Us Features',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='WhyChooseHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default='Why Choose Us', max_length=100)),
                ('title', models.CharField(default='Excellence in Every Service', max_length=200)),
                ('image', models.ImageField(upload_to='whychooseus/')),
            ],
            options={
                'verbose_name': 'Why Choose Us Header',
                'verbose_name_plural': 'Why Choose Us Header',
            },
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday_hours', models.CharField(default='9:00 AM - 6:00 PM', max_length=50)),
                ('saturday_hours', models.CharField(default='10:00 AM - 4:00 PM', max_length=50)),
                ('sunday_status', models.CharField(default='Closed', max_length=50)),
            ],
            options={
                'verbose_name': 'Working Hours',
                'verbose_name_plural': 'Working Hours',
            },
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_requests', to='homepage.service')),
            ],
            options={
                'verbose_name': 'Contact Form',
                'verbose_name_plural': 'Contact Forms',
                'ordering': ['-created_at'],
            },
        ),
    ]