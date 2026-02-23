"""
URL configuration for devapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # ── Legacy / dead-URL redirects (302) ─────────────────────────────
    # Catch-all: any /product/<anything> → /products/  (covers ketoconazole, pregabalin, etc.)
    re_path(r'^product/.+$', RedirectView.as_view(url='/products/', permanent=False)),
    re_path(r'^blog/.+$', RedirectView.as_view(url='/insights/', permanent=False)),
    re_path(r'^static/media/VCP-003-TDS\.pdf$', RedirectView.as_view(url='/products/', permanent=False)),
    path('', views.index, name='index'),
    path('aboutus/', views.about, name='aboutus'),
    path('ourservices/', views.ourservices, name='ourservices'),
    path('products/', views.products, name='products'),
    path('articles/', views.article_list, name='article_list'),
    path('insights/', views.insights_list, name='insights_list'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('insights/<slug:slug>/', views.insight_detail, name='insight_detail'),
]

