from .models import Profile


def profile_processor(request):
    """Make the site profile and unread message count available to all templates."""
    profile = Profile.objects.first()
    return {
        'site_profile': profile,
    }