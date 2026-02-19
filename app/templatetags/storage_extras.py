from django import template
from django.core.files.storage import default_storage

register = template.Library()


@register.filter
def file_exists(name):
    """Return True if the given storage path exists."""
    try:
        if not name:
            return False
        return default_storage.exists(name)
    except Exception:
        return False
