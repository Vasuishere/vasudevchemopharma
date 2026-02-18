from django.db import models


class ProductCategory(models.Model):
    """Filter-nav categories (Industrial Chemicals, APIs, Specialty, etc.)."""
    slug = models.SlugField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    # Overview-card fields (shown in the "Product Categories" section)
    icon_class = models.CharField(
        max_length=100, blank=True, default="",
        help_text='Bootstrap icon class, e.g. "bi bi-gear-fill"',
    )
    overview_title = models.CharField(max_length=150, blank=True, default="")
    overview_description = models.TextField(blank=True, default="")
    show_in_overview = models.BooleanField(
        default=False,
        help_text="Display this category in the overview grid on the products page",
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.label


class Product(models.Model):
    """Individual product card on the products page."""
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="products",
    )
    slug = models.SlugField(max_length=220, unique=True)
    icon = models.CharField(
        max_length=10,
        help_text='Short symbol shown in the circle, e.g. "H2S"',
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            import uuid
            base = slugify(self.name)
            if not base:
                base = uuid.uuid4().hex[:8]
            candidate = base
            suffix = 1
            qs = self.__class__.objects.filter(slug=candidate).exclude(pk=self.pk)
            while qs.exists():
                candidate = f"{base}-{suffix}"
                qs = self.__class__.objects.filter(slug=candidate).exclude(pk=self.pk)
                suffix += 1
            self.slug = candidate

        from django.db import IntegrityError
        try:
            super().save(*args, **kwargs)
        except IntegrityError:
            # Handle race condition: regenerate slug and retry once
            import uuid
            self.slug = f"{self.slug}-{uuid.uuid4().hex[:6]}"
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'slug': self.slug})


class ProductSpec(models.Model):
    """Key-value specification row displayed on a product card."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="specs",
    )
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.product.name} – {self.label}: {self.value}"
