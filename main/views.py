from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Project, ContactMessage, Resume, Profile, Skill,
    Experience, Education, Achievement, Technology
)
from .forms import ContactForm


def get_or_default_profile():
    """Get the site profile or return a default one."""
    profile = Profile.objects.first()
    return profile


def home(request):
    featured_projects = Project.objects.filter(featured=True, image__isnull=False)[:3]
    if not featured_projects.exists():
        featured_projects = Project.objects.all()[:3]
    profile = get_or_default_profile()
    skills = Skill.objects.filter(is_active=True)
    experiences = Experience.objects.filter(is_active=True)[:3]
    achievements = Achievement.objects.filter(is_active=True)[:3]
    # Stats for measurable hero metrics
    total_projects = Project.objects.count()
    total_skills = Skill.objects.filter(is_active=True).count()
    total_experience_years = Experience.objects.filter(is_active=True).count() * 2  # rough estimate
    context = {
        'featured_projects': featured_projects,
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'achievements': achievements,
        'total_projects': total_projects,
        'total_skills': total_skills,
        'total_experience_years': total_experience_years,
        'is_homepage': True,
    }
    return render(request, "home.html", context)


def projects(request):
    all_projects = Project.objects.all().order_by('-created_at')
    profile = get_or_default_profile()
    return render(request, 'projects.html', {
        'projects': all_projects,
        'profile': profile,
    })


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(pk=project.pk)[:3]
    return render(request, 'project_detail.html', {
        'project': project,
        'related_projects': related_projects,
    })


def resume(request):
    resumes = Resume.objects.all().order_by('-uploaded_at')
    resume_file = resumes.first()  # Get latest resume
    profile = get_or_default_profile()
    experiences = Experience.objects.filter(is_active=True)
    education = Education.objects.filter(is_active=True)
    achievements = Achievement.objects.filter(is_active=True)
    skills = Skill.objects.filter(is_active=True)[:12]
    return render(request, 'resume.html', {
        'resume': resume_file,
        'profile': profile,
        'experiences': experiences,
        'education_list': education,
        'achievements': achievements,
        'skills': skills,
    })


def contact(request):
    profile = get_or_default_profile()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save message
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            # Send email notification (if email settings are configured)
            if settings.DEFAULT_FROM_EMAIL:
                try:
                    send_mail(
                        subject=f"New Contact from {form.cleaned_data['name']}",
                        message=form.cleaned_data['message'],
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.DEFAULT_FROM_EMAIL],
                        fail_silently=True,
                    )
                except Exception:
                    pass  # Don't block the user if email fails
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'profile': profile,
    })


def contact_success(request):
    return render(request, 'contact_success.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
