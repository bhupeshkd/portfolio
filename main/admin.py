from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, Project, Technology, Skill, Experience,
    Education, Achievement, Resume, ContactMessage
)

# ============================================
# Profile Admin
# ============================================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Single-instance profile with picture preview."""
    list_display = ('name', 'title', 'email', 'location', 'available', 'updated_at')
    list_editable = ('available',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'profile_picture', 'about_text')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Availability', {
            'fields': ('available', 'available_text')
        }),
    )

    def has_add_permission(self, request):
        if Profile.objects.exists() and not request.GET.get('_add'):
            return False
        return True


# ============================================
# Technology Admin
# ============================================
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'project_count')
    search_fields = ['name']
    list_per_page = 25

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="{}" style="font-size: 18px;"></i>', obj.icon)
        return '-'
    icon_preview.short_description = 'Icon'

    def project_count(self, obj):
        return obj.projects.count()
    project_count.short_description = 'Projects'


# ============================================
# Project Admin
# ============================================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'category', 'featured', 'tech_count', 'created_at', 'updated_at')
    list_filter = ('category', 'featured', 'technologies', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    list_editable = ('featured',)
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    list_per_page = 20

    fieldsets = (
        ('Project Details', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Media', {
            'fields': ('image', 'image_preview')
        }),
        ('Links', {
            'fields': ('github_link', 'live_link')
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
        ('Settings', {
            'fields': ('featured', 'created_at', 'updated_at')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 6px;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Preview'

    def tech_count(self, obj):
        return obj.technologies.count()
    tech_count.short_description = 'Tech Stack'


# ============================================
# Skill Admin
# ============================================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'percentage', 'percentage_bar', 'display_order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('percentage', 'display_order', 'is_active')
    search_fields = ('name',)
    list_per_page = 25

    def percentage_bar(self, obj):
        color = '#10b981' if obj.percentage >= 70 else '#f59e0b' if obj.percentage >= 40 else '#ef4444'
        return format_html(
            '<div style="background: #e2e8f0; border-radius: 4px; width: 120px; height: 8px;">'
            '<div style="background: {}; width: {}%; height: 8px; border-radius: 4px;"></div>'
            '</div> <span style="font-size: 12px; color: #64748b;">{}%</span>',
            color, obj.percentage, obj.percentage
        )
    percentage_bar.short_description = 'Proficiency'


# ============================================
# Experience Admin
# ============================================
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    search_fields = ('position', 'company')
    list_per_page = 20


# ============================================
# Education Admin
# ============================================
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    search_fields = ('degree', 'institution')
    list_per_page = 20


# ============================================
# Achievement Admin
# ============================================
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    list_per_page = 20

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="{}" style="font-size: 16px;"></i>', obj.icon)
        return '-'
    icon_preview.short_description = 'Icon'


# ============================================
# Resume Admin
# ============================================
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_link', 'uploaded_at')
    readonly_fields = ('uploaded_at',)

    def file_link(self, obj):
        return format_html('<a href="{}" target="_blank"><i class="fas fa-file-pdf"></i> View</a>', obj.file.url)
    file_link.short_description = 'File'


# ============================================
# Contact Message Admin
# ============================================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_short', 'message_preview', 'status_badge', 'sent_at')
    list_filter = ('is_read', 'sent_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'sent_at')
    list_per_page = 25
    actions = ['mark_as_read', 'mark_as_unread']

    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'message', 'sent_at', 'is_read')
        }),
    )

    def email_short(self, obj):
        if len(obj.email) > 25:
            return obj.email[:22] + '...'
        return obj.email
    email_short.short_description = 'Email'

    def message_preview(self, obj):
        if len(obj.message) > 60:
            return obj.message[:57] + '...'
        return obj.message
    message_preview.short_description = 'Message'

    def status_badge(self, obj):
        if obj.is_read:
            return format_html(
                '<span style="background: #dcfce7; color: #166534; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">✓ Read</span>'
            )
        return format_html(
            '<span style="background: #fef3c7; color: #92400e; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">● New</span>'
        )
    status_badge.short_description = 'Status'

    @admin.action(description='Mark as read')
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} message(s) marked as read.')

    @admin.action(description='Mark as unread')
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} message(s) marked as unread.')


# ============================================
# Custom Admin Dashboard
# ============================================
# Store the original admin index method
_original_admin_index = admin.site.index


def _custom_admin_index(request, extra_context=None):
    """Custom admin dashboard with portfolio stats."""
    if extra_context is None:
        extra_context = {}
    # Generate dashboard stats
    recent_messages = ContactMessage.objects.all()[:5]
    latest_resume = Resume.objects.first()
    extra_context.update({
        'projects_count': Project.objects.count(),
        'featured_count': Project.objects.filter(featured=True).count(),
        'web_count': Project.objects.filter(category='web').count(),
        'messages_count': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'skills_count': Skill.objects.count(),
        'active_skills': Skill.objects.filter(is_active=True).count(),
        'resumes_count': Resume.objects.count(),
        'latest_resume': latest_resume,
        'recent_messages': recent_messages,
    })
    return _original_admin_index(request, extra_context=extra_context)


# Override the admin index with custom dashboard context
admin.site.index = _custom_admin_index

# Custom branding
admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin Panel'
admin.site.index_title = 'Dashboard - Manage Your Portfolio'