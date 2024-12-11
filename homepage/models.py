from django.db import models

class ContactInfo(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    site_name=models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Contact Information"
    
    class Meta:
        verbose_name_plural = "Contact Information"

class SocialMedia(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_icons/')
    
    def __str__(self):
        return self.platform
    
    class Meta:
        verbose_name_plural = "Social Media Links"

class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.alt_text

    class Meta:
        verbose_name_plural = "Logo"

class HeroSlide(models.Model):
    title_highlight = models.CharField(max_length=100, help_text="Text with gradient effect")
    title_main = models.CharField(max_length=200, help_text="Main title text")
    description = models.TextField(max_length=500)
    description_highlight = models.CharField(max_length=200, help_text="Highlighted text in description")
    image = models.ImageField(upload_to='hero_slides/')
    button_text = models.CharField(max_length=50, default="Book Our Services")
    button_url = models.CharField(max_length=200, default="#contact")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Hero Slide {self.order}: {self.title_main}"

    class Meta:
        ordering = ['order']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='services/')
    button_text = models.CharField(max_length=50, default="Book Us")
    button_url = models.CharField(max_length=200, default="#contact")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"

class ServiceHeader(models.Model):
    subtitle = models.CharField(max_length=100, default="Our Services")
    title = models.CharField(max_length=200, default="Professional Solutions")
    
    def __str__(self):
        return "Service Section Header"
    
    class Meta:
        verbose_name = "Service Section Header"
        verbose_name_plural = "Service Section Header"

    
class WhyChooseHeader(models.Model):
    subtitle = models.CharField(max_length=100, default="Why Choose Us")
    title = models.CharField(max_length=200, default="Excellence in Every Service")
    image=models.ImageField(upload_to='whychooseus/')
    def __str__(self):
        return "Why Choose Us Header"
    
    class Meta:
        verbose_name = "Why Choose Us Header"
        verbose_name_plural = "Why Choose Us Header"

class WhyChooseFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    icon_class = models.ImageField(upload_to='whychooseus/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Why Choose Us Feature"
        verbose_name_plural = "Why Choose Us Features"

class AboutUsHeader(models.Model):
    subtitle = models.CharField(max_length=100, default="About Us")
    title = models.CharField(max_length=200, default="Your Trusted Service Partner")
    
    def __str__(self):
        return "About Us Header"
    
    class Meta:
        verbose_name = "About Us Header"
        verbose_name_plural = "About Us Header"

class AboutCount(models.Model):
    icon_class = models.CharField(max_length=1000)
    count_value = models.IntegerField()
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
        verbose_name = "About Count"
        verbose_name_plural = "About Counts"

class TeamHeader(models.Model):
    subtitle = models.CharField(max_length=100, default="Our Team")
    title = models.CharField(max_length=200, default="Meet Our Expert Team")
    
    def __str__(self):
        return "Team Section Header"
    
    class Meta:
        verbose_name = "Team Section Header"
        verbose_name_plural = "Team Section Header"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

class ContactHeader(models.Model):
    subtitle = models.CharField(max_length=100, default="Let's Connect")
    title = models.CharField(max_length=200, default="Get in Touch")
    description = models.TextField(max_length=300, default="Let's create something amazing together")
    
    def __str__(self):
        return "Contact Section Header"
    
    class Meta:
        verbose_name = "Contact Section Header"
        verbose_name_plural = "Contact Section Header"

class WorkingHours(models.Model):
    weekday_hours = models.CharField(max_length=50, default="9:00 AM - 6:00 PM")
    saturday_hours = models.CharField(max_length=50, default="10:00 AM - 4:00 PM")
    sunday_status = models.CharField(max_length=50, default="Closed")
    
    def __str__(self):
        return "Working Hours"
    
    class Meta:
        verbose_name = "Working Hours"
        verbose_name_plural = "Working Hours"






class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.CharField(max_length=10)
    service = models.ForeignKey(
        Service, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='contact_requests'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Contact from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"



class EmailRecipient(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Email Recipient"
        verbose_name_plural = "Email Recipients"