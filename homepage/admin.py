from django.contrib import admin
from .models import ContactInfo, SocialMedia, Logo, HeroSlide, Service, ServiceHeader, WhyChooseHeader, WhyChooseFeature, AboutUsHeader, AboutCount, TeamHeader, TeamMember, WorkingHours, ContactHeader, ContactForm,EmailRecipient

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')
    list_display_links = ('platform',)
    search_fields = ('platform',)

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title_main', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title_main', 'title_highlight', 'description')
    list_filter = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Title Section', {
            'fields': ('title_highlight', 'title_main')
        }),
        ('Description', {
            'fields': ('description', 'description_highlight')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Button', {
            'fields': ('button_text', 'button_url')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Service Information', {
            'fields': ('title', 'description')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Button Settings', {
            'fields': ('button_text', 'button_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(ServiceHeader)
class ServiceHeaderAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'title')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True

@admin.register(WhyChooseHeader)
class WhyChooseHeaderAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'title')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True
    
    fieldsets = (
        ('Section Headers', {
            'fields': ('subtitle', 'title')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

@admin.register(WhyChooseFeature)
class WhyChooseFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Feature Information', {
            'fields': ('title', 'description')
        }),
        ('Icon', {
            'fields': ('icon_class',),
            'description': 'Enter The Image'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(AboutUsHeader)
class AboutUsHeaderAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'title')
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

@admin.register(AboutCount)
class AboutCountAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_value', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Counter Information', {
            'fields': ('title', 'count_value')
        }),
        ('Icon', {
            'fields': ('icon_class',),
            'description': 'Enter the SVG icon class or code for the counter'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(TeamHeader)
class TeamHeaderAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'title')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'position')
    list_filter = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'image')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url'),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(ContactHeader)
class ContactHeaderAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'title')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True
    
    fieldsets = (
        ('Section Headers', {
            'fields': ('subtitle', 'title')
        }),
        ('Content', {
            'fields': ('description',)
        }),
    )

@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ('weekday_hours', 'saturday_hours', 'sunday_status')
    
    def has_add_permission(self, request):
        # Allow only one instance
        if self.model.objects.exists():
            return False
        return True

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'created_at', 'is_read')
    list_filter = ('is_read', 'service', 'created_at')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_at'
    list_editable = ('is_read',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message Details', {
            'fields': ('service', 'message')
        }),
        ('Status', {
            'fields': ('is_read',)
        })
    )
    
    def has_add_permission(self, request):
        return False  # Prevent manual creation in admin




@admin.register(EmailRecipient)
class EmailRecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    ordering = ('-created_at',)