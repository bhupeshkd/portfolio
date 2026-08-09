from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    """Site owner profile - manage from admin panel."""
    name = models.CharField(max_length=100, default='Bhupesh Dewangan')
    title = models.CharField(max_length=200, default='Python & Django Developer')
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    about_text = models.TextField(blank=True)
    email = models.EmailField(default='bhupeshdeww@gmail.com')
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, default='Chhattisgarh, India')
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    available = models.BooleanField(default=True)
    available_text = models.CharField(max_length=100, default='Available for work')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure only one profile exists
        if not self.pk and Profile.objects.exists():
            existing = Profile.objects.first()
            self.pk = existing.pk
            self.id = existing.id
        super().save(*args, **kwargs)


class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class (e.g. fab fa-python)')

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('app', 'Mobile App'),
        ('script', 'Automation/Script'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name="projects", blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text='Project banner/cover image')
    featured = models.BooleanField(default=False, help_text='Pin to featured section on home page')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Manage skills from admin - shown on home page."""
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('backend', 'Backend'),
            ('frontend', 'Frontend'),
            ('database', 'Databases'),
            ('tools', 'Tools'),
        ],
        default='backend'
    )
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class')
    percentage = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        default=80,
        help_text='Skill proficiency percentage'
    )
    display_order = models.IntegerField(default=0, help_text='Lower = appears first')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Experience(models.Model):
    """Work experience - shown on resume page."""
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=50, help_text='e.g. 2024 - Present')
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=300, blank=True, help_text='Comma-separated tech tags')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = "Experiences"

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def __str__(self):
        return f"{self.position} - {self.start_date}"


class Education(models.Model):
    """Education - shown on resume page."""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50, help_text='e.g. 2024 - Present')
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Achievement(models.Model):
    """Achievements - shown on resume page."""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=100, default='My Resume')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.name} - {self.email}"