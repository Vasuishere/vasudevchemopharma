from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .insights_data import INSIGHTS_BY_SLUG
from .models import Product, ProductCategory, ProductArticle, CompanyDetails

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def ourservices(request):
    return render(request, 'ourservices.html')

def products(request):
    all_categories = ProductCategory.objects.all()
    context = {
        'products': Product.objects.select_related('category').prefetch_related('specs').all(),
        'categories': all_categories,
        'category_overview': all_categories.filter(show_in_overview=True),
    }
    return render(request, 'products.html', context)


def product_detail(request, slug):
    try:
        product = (
            Product.objects
            .select_related('category')
            .prefetch_related('specs', 'images', 'documents', 'faqs', 'pricing_tiers')
            .get(slug=slug)
        )
    except Product.DoesNotExist:
        raise Http404("Product not found")

    related_products = (
        Product.objects
        .filter(category=product.category)
        .exclude(pk=product.pk)
        .select_related('category')[:3]
    )

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)


def insight_detail(request, slug):
    article = INSIGHTS_BY_SLUG.get(slug)
    if article is None:
        raise Http404("Insight not found")
    return render(request, 'insight_detail.html', {'article': article})


def article_list(request):
    articles = ProductArticle.objects.filter(is_published=True)
    return render(request, 'articles.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(ProductArticle, slug=slug, is_published=True)
    related_articles = (
        ProductArticle.objects
        .filter(is_published=True)
        .exclude(pk=article.pk)[:3]
    )
    promoted_products = article.promoted_products.select_related('category').all()[:8]
    company = CompanyDetails.load()
    context = {
        'article': article,
        'related_articles': related_articles,
        'promoted_products': promoted_products,
        'company': company,
    }
    return render(request, 'article_detail.html', context)