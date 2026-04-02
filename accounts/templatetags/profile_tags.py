from django import template
from accounts.models import Profile

register = template.Library()

@register.simple_tag
def get_profile(user):
    if not user or not user.is_authenticated:
        return None
    try:
        return user.profile
    except Profile.DoesNotExist:
        profile, _ = Profile.objects.get_or_create(user=user)
        return profile
