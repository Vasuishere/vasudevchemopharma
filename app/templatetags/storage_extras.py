from django import template
from django.core.files.storage import default_storage

register = template.Library()


@register.simple_tag
def file_exists(name):
    """Return True if the given storage path exists.

    Usage in template:
      {% load storage_extras %}
      {% if company.company_logo and file_exists company.company_logo.name %}
          <img src="{{ company.company_logo.url }}">...
      {% endif %}
    """
    try:
        if not name:
            return False
        return default_storage.exists(name)
    except Exception:
        return False
