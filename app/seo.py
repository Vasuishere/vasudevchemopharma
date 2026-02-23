"""
SEO helpers – robots.txt and dynamic XML sitemap for Google / Bing crawlers.
"""

from datetime import date
from xml.sax.saxutils import escape

from django.http import HttpResponse
from django.urls import reverse
from .models import Product, ProductArticle
from .insights_data import INSIGHTS

DOMAIN = "https://vasudevchemopharma.com"


def robots_txt(request):
    """Serve robots.txt as plain text."""
    sitemap_url = f"{DOMAIN}{reverse('sitemap_xml')}"
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "# Disallow admin and internal paths",
        "Disallow: /admin/",
        "",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")


def sitemap_xml(request):
    """Generate a dynamic XML sitemap containing every public URL."""

    today = date.today().isoformat()

    urls = []

    # ── Static pages ──────────────────────────────────────────────────
    static_pages = [
        {"loc": "/", "changefreq": "weekly", "priority": "1.0"},
        {"loc": "/aboutus/", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/ourservices/", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "/products/", "changefreq": "weekly", "priority": "0.9"},
        {"loc": "/insights/", "changefreq": "weekly", "priority": "0.8"},
        {"loc": "/articles/", "changefreq": "weekly", "priority": "0.7"},
    ]
    for page in static_pages:
        urls.append(
            f"  <url>\n"
            f"    <loc>{DOMAIN}{page['loc']}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{page['changefreq']}</changefreq>\n"
            f"    <priority>{page['priority']}</priority>\n"
            f"  </url>"
        )

    # ── Product detail pages (from database) ──────────────────────────
    for slug in Product.objects.values_list("slug", flat=True):
        loc = escape(f"{DOMAIN}/products/{slug}/")
        urls.append(
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>weekly</changefreq>\n"
            f"    <priority>0.8</priority>\n"
            f"  </url>"
        )

    # ── Article detail pages (from database) ────────────────────────
    for slug in ProductArticle.objects.filter(is_published=True).values_list("slug", flat=True):
        loc = escape(f"{DOMAIN}/articles/{slug}/")
        urls.append(
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>weekly</changefreq>\n"
            f"    <priority>0.7</priority>\n"
            f"  </url>"
        )

    # ── Insight articles (from static data) ───────────────────────────
    for article in INSIGHTS:
        loc = escape(f"{DOMAIN}/insights/{article['slug']}/")
        urls.append(
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.7</priority>\n"
            f"  </url>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    return HttpResponse(xml, content_type="application/xml; charset=utf-8")
