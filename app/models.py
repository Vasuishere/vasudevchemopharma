from django.db import models


class ProductCategory(models.Model):
    """Filter-nav categories (Industrial Chemicals, APIs, Specialty, etc.)."""
    slug = models.SlugField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
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


# ─────────────────────────────────────────────────────────────────────
# Product
# ─────────────────────────────────────────────────────────────────────

class Product(models.Model):
    """Comprehensive product model – all optional fields are blank/null-safe."""

    SIGNAL_WORD_CHOICES = [
        ("", "— Not set —"),
        ("Danger", "Danger"),
        ("Warning", "Warning"),
    ]

    # ── 1. Basic Information ──────────────────────────────────────────
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="products",
    )
    slug = models.SlugField(max_length=220, unique=True)
    icon = models.CharField(
        max_length=10, blank=True, default="",
        help_text='Short symbol for the icon circle, e.g. "H2S"',
    )
    name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200, blank=True, default="")
    manufacturer = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField(
        help_text="Short description shown on product cards",
    )
    full_description = models.TextField(
        blank=True, default="",
        help_text="Detailed description shown on the product detail page",
    )
    sku = models.CharField(
        max_length=100, blank=True, default="",
        verbose_name="SKU / Product Code",
    )
    cas_number = models.CharField(
        max_length=50, blank=True, default="",
        verbose_name="CAS Number",
    )
    hs_code = models.CharField(
        max_length=50, blank=True, default="",
        verbose_name="HS Code",
    )
    pack_sizes = models.TextField(
        blank=True, default="",
        help_text="Available pack sizes – one per line",
    )
    country_of_origin = models.CharField(max_length=100, blank=True, default="")

    # ── 2. Chemical Identification ────────────────────────────────────
    common_names = models.TextField(
        blank=True, default="",
        help_text="Synonyms – one per line",
        verbose_name="Common Name / Synonyms",
    )
    molecular_formula = models.CharField(max_length=200, blank=True, default="")
    molecular_weight = models.CharField(max_length=100, blank=True, default="")
    structure_image = models.ImageField(
        upload_to="products/structures/", blank=True, null=True,
        verbose_name="Structure Formula Image",
    )
    purity_grade = models.CharField(
        max_length=200, blank=True, default="",
        verbose_name="Purity / Grade",
    )
    is_technical_grade = models.BooleanField(default=False, verbose_name="Technical Grade")
    is_industrial_grade = models.BooleanField(default=False, verbose_name="Industrial Grade")
    is_analytical_grade = models.BooleanField(default=False, verbose_name="Analytical Grade")
    is_pharma_grade = models.BooleanField(default=False, verbose_name="Pharma Grade")
    un_number = models.CharField(
        max_length=50, blank=True, default="",
        verbose_name="UN Number",
    )

    # ── 3. Safety & Regulatory ────────────────────────────────────────
    ghs_classification = models.TextField(
        blank=True, default="",
        verbose_name="GHS Hazard Classification",
    )
    hazard_statements = models.TextField(
        blank=True, default="",
        help_text="H-codes – one per line",
    )
    precautionary_statements = models.TextField(
        blank=True, default="",
        help_text="P-codes – one per line",
    )
    hazard_pictograms = models.CharField(
        max_length=500, blank=True, default="",
        help_text='GHS pictogram codes separated by commas, e.g. "GHS02, GHS07"',
    )
    signal_word = models.CharField(
        max_length=20, blank=True, default="",
        choices=SIGNAL_WORD_CHOICES,
    )
    sds_file = models.FileField(
        upload_to="products/sds/", blank=True, null=True,
        verbose_name="Safety Data Sheet (SDS)",
    )
    transport_class = models.CharField(max_length=50, blank=True, default="")
    packing_group = models.CharField(max_length=50, blank=True, default="")
    flash_point = models.CharField(max_length=100, blank=True, default="")
    storage_conditions = models.TextField(blank=True, default="")
    handling_instructions = models.TextField(blank=True, default="")
    disposal_information = models.TextField(blank=True, default="")
    regulatory_compliance = models.TextField(blank=True, default="")
    iso_certification = models.CharField(max_length=200, blank=True, default="")

    # ── 4. Physical & Chemical Properties ─────────────────────────────
    appearance = models.CharField(max_length=200, blank=True, default="")
    odor = models.CharField(max_length=200, blank=True, default="")
    density = models.CharField(max_length=100, blank=True, default="")
    melting_point = models.CharField(max_length=100, blank=True, default="")
    boiling_point = models.CharField(max_length=100, blank=True, default="")
    solubility = models.TextField(blank=True, default="")
    ph_value = models.CharField(
        max_length=50, blank=True, default="",
        verbose_name="pH",
    )
    vapor_pressure = models.CharField(max_length=100, blank=True, default="")
    viscosity = models.CharField(max_length=100, blank=True, default="")
    refractive_index = models.CharField(max_length=100, blank=True, default="")
    stability_reactivity = models.TextField(
        blank=True, default="",
        verbose_name="Stability / Reactivity",
    )

    # ── 5. Application & Usage ────────────────────────────────────────
    primary_applications = models.TextField(blank=True, default="")
    industry_usage = models.TextField(
        blank=True, default="",
        help_text="e.g. Pharma, Textile, Paint, Agriculture …",
    )
    recommended_dosage = models.TextField(
        blank=True, default="",
        verbose_name="Recommended Dosage / Usage Rate",
    )
    compatible_materials = models.TextField(blank=True, default="")
    shelf_life = models.CharField(max_length=100, blank=True, default="")

    # ── 6. Packaging & Logistics ──────────────────────────────────────
    net_weight = models.CharField(max_length=100, blank=True, default="")
    gross_weight = models.CharField(max_length=100, blank=True, default="")
    packaging_type = models.CharField(
        max_length=200, blank=True, default="",
        help_text="Drum, Bottle, Bag, Tanker, etc.",
    )
    dimensions = models.CharField(max_length=200, blank=True, default="")
    moq = models.CharField(
        max_length=100, blank=True, default="",
        verbose_name="Minimum Order Quantity (MOQ)",
    )
    lead_time = models.CharField(max_length=100, blank=True, default="")
    shipping_restrictions = models.TextField(blank=True, default="")
    dangerous_goods = models.BooleanField(
        default=None, null=True, blank=True,
        verbose_name="Dangerous Goods",
    )

    # ── 8. Commercial ────────────────────────────────────────────────
    customer_support_contact = models.TextField(blank=True, default="")
    batch_traceability = models.TextField(
        blank=True, default="",
        verbose_name="Batch Traceability Info",
    )

    # ── 9. SEO ────────────────────────────────────────────────────────
    seo_title = models.CharField(
        max_length=300, blank=True, default="",
        verbose_name="SEO Page Title",
        help_text="Custom page <title> for search engines. Leave blank to use product name.",
    )
    meta_keywords = models.TextField(
        blank=True, default="",
        verbose_name="Meta Keywords / Tags",
        help_text="Comma-separated keywords for meta tags and SEO.",
    )
    meta_description_seo = models.TextField(
        blank=True, default="",
        verbose_name="SEO Meta Description",
        help_text="Custom meta description for search engines. Leave blank to use short description.",
    )
    seo_h1 = models.CharField(
        max_length=300, blank=True, default="",
        verbose_name="SEO H1 Heading",
        help_text="Custom H1 heading for the product page. Leave blank to use product name.",
    )
    seo_h2_tags = models.TextField(
        blank=True, default="",
        verbose_name="SEO H2 Sub-headings",
        help_text="One per line. Rendered as hidden H2 headings on the page for SEO.",
    )
    seo_rich_text = models.TextField(
        blank=True, default="",
        verbose_name="SEO Rich Content",
        help_text="Keyword-rich content block rendered on the product page (below overview) for Google indexing.",
    )

    # ── Ordering ──────────────────────────────────────────────────────
    order = models.PositiveIntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    # ── slug auto-generation ──────────────────────────────────────────
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
            import uuid
            self.slug = f"{self.slug}-{uuid.uuid4().hex[:6]}"
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'slug': self.slug})

    # ── Section-availability helpers (used in templates) ──────────────
    @property
    def primary_image(self):
        img = self.images.filter(is_primary=True).first()
        return img or self.images.first()

    @property
    def available_grades(self):
        g = []
        if self.is_technical_grade:
            g.append("Technical")
        if self.is_industrial_grade:
            g.append("Industrial")
        if self.is_analytical_grade:
            g.append("Analytical")
        if self.is_pharma_grade:
            g.append("Pharma")
        return g

    @property
    def pack_sizes_list(self):
        return [s.strip() for s in self.pack_sizes.splitlines() if s.strip()] if self.pack_sizes else []

    @property
    def common_names_list(self):
        return [s.strip() for s in self.common_names.splitlines() if s.strip()] if self.common_names else []

    @property
    def hazard_statements_list(self):
        return [s.strip() for s in self.hazard_statements.splitlines() if s.strip()] if self.hazard_statements else []

    @property
    def precautionary_statements_list(self):
        return [s.strip() for s in self.precautionary_statements.splitlines() if s.strip()] if self.precautionary_statements else []

    @property
    def hazard_pictograms_list(self):
        return [s.strip() for s in self.hazard_pictograms.split(',') if s.strip()] if self.hazard_pictograms else []

    @property
    def has_chemical_identification(self):
        return any([
            self.common_names, self.molecular_formula, self.molecular_weight,
            self.structure_image, self.purity_grade, self.un_number,
            self.is_technical_grade, self.is_industrial_grade,
            self.is_analytical_grade, self.is_pharma_grade,
        ])

    @property
    def has_safety_info(self):
        return any([
            self.ghs_classification, self.hazard_statements,
            self.precautionary_statements, self.hazard_pictograms,
            self.signal_word, self.sds_file, self.transport_class,
            self.packing_group, self.flash_point, self.storage_conditions,
            self.handling_instructions, self.disposal_information,
            self.regulatory_compliance, self.iso_certification,
        ])

    @property
    def has_physical_properties(self):
        return any([
            self.appearance, self.odor, self.density, self.melting_point,
            self.boiling_point, self.solubility, self.ph_value,
            self.vapor_pressure, self.viscosity, self.refractive_index,
            self.stability_reactivity,
        ])

    @property
    def has_application_info(self):
        return any([
            self.primary_applications, self.industry_usage,
            self.recommended_dosage, self.compatible_materials, self.shelf_life,
        ])

    @property
    def has_packaging_info(self):
        return any([
            self.net_weight, self.gross_weight, self.packaging_type,
            self.dimensions, self.moq, self.lead_time,
            self.shipping_restrictions,
        ]) or self.dangerous_goods is not None

    @property
    def seo_h2_list(self):
        """Return SEO H2 sub-headings as a list."""
        return [s.strip() for s in self.seo_h2_tags.splitlines() if s.strip()] if self.seo_h2_tags else []

    @property
    def meta_keywords_list(self):
        """Return meta keywords as a list."""
        return [s.strip() for s in self.meta_keywords.split(',') if s.strip()] if self.meta_keywords else []


# ─────────────────────────────────────────────────────────────────────
# Related models (inlines)
# ─────────────────────────────────────────────────────────────────────

class ProductSpec(models.Model):
    """Additional key-value specification row."""
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


class ProductImage(models.Model):
    """Multiple images per product (gallery)."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images",
    )
    image = models.ImageField(upload_to="products/images/")
    alt_text = models.CharField(max_length=200, blank=True, default="")
    is_primary = models.BooleanField(
        default=False,
        help_text="Show this image as the main product image",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.product.name} – image {self.order}"


class ProductDocument(models.Model):
    """Downloadable documents (COA, TDS, SDS, certificates, etc.)."""
    DOC_TYPE_CHOICES = [
        ("COA", "Certificate of Analysis"),
        ("TDS", "Technical Data Sheet"),
        ("SDS", "Safety Data Sheet (SDS)"),
        ("MSDS", "Material Safety Data Sheet (MSDS)"),
        ("ISO", "ISO Certificate"),
        ("GMP", "GMP Certificate"),
        ("HALAL", "Halal Certificate"),
        ("KOSHER", "Kosher Certificate"),
        ("OTHER", "Other"),
    ]
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="documents",
    )
    title = models.CharField(max_length=200)
    doc_type = models.CharField(
        max_length=10, choices=DOC_TYPE_CHOICES, default="OTHER",
        verbose_name="Document Type",
    )
    file = models.FileField(upload_to="products/documents/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.product.name} – {self.get_doc_type_display()}"

    @property
    def icon_class(self):
        icons = {
            "COA": "bi-file-earmark-medical",
            "TDS": "bi-file-earmark-bar-graph",
            "SDS": "bi-shield-exclamation",
            "MSDS": "bi-shield-exclamation",
            "ISO": "bi-award",
            "GMP": "bi-patch-check",
            "HALAL": "bi-check-circle",
            "KOSHER": "bi-check-circle",
            "OTHER": "bi-file-earmark",
        }
        return icons.get(self.doc_type, "bi-file-earmark")


class ProductFAQ(models.Model):
    """Per-product FAQ entries."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="faqs",
    )
    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return f"{self.product.name} – {self.question[:60]}"


class ProductPricingTier(models.Model):
    """Bulk pricing indication rows."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="pricing_tiers",
    )
    min_quantity = models.CharField(max_length=100)
    max_quantity = models.CharField(max_length=100, blank=True, default="")
    price_info = models.CharField(
        max_length=200,
        help_text='Descriptive (e.g. "Contact for pricing", "₹120/kg")',
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Pricing Tier"

    def __str__(self):
        return f"{self.product.name} – {self.min_quantity}+"


# ─────────────────────────────────────────────────────────────────────
# Company Details  (singleton – only one row expected)
# ─────────────────────────────────────────────────────────────────────
class CompanyDetails(models.Model):
    """Single-row table that stores all company-wide information."""

    # ── Branding ──────────────────────────────────────────────────────
    company_name = models.CharField(max_length=200, default="Vasudev Chemo Pharma")
    company_logo = models.ImageField(
        upload_to="company/", blank=True, null=True,
        help_text="Primary company logo (used in header, footer, etc.)",
    )
    company_name_image = models.ImageField(
        upload_to="company/", blank=True, null=True,
        help_text="Company name as an image / wordmark",
    )
    tagline = models.CharField(
        max_length=300, blank=True, default="",
        help_text="Short tagline / slogan",
    )
    about_short = models.TextField(
        blank=True, default="",
        help_text="Short description (shown in footer, etc.)",
    )

    # ── Contact — Phone Numbers ───────────────────────────────────────
    phone_primary = models.CharField(max_length=30, blank=True, default="")
    phone_secondary = models.CharField(
        max_length=30, blank=True, default="",
        help_text="Sales team / alternate number",
    )
    phone_export = models.CharField(
        max_length=30, blank=True, default="",
        help_text="Export enquiry phone number",
    )

    # ── Contact — Emails ──────────────────────────────────────────────
    email_general = models.EmailField(blank=True, default="")
    email_sales = models.EmailField(blank=True, default="")
    email_export = models.EmailField(blank=True, default="")
    email_support = models.EmailField(blank=True, default="")

    # ── Address ───────────────────────────────────────────────────────
    address_line1 = models.CharField(max_length=200, blank=True, default="")
    address_line2 = models.CharField(max_length=200, blank=True, default="")
    city = models.CharField(max_length=100, blank=True, default="")
    state = models.CharField(max_length=100, blank=True, default="")
    country = models.CharField(max_length=100, blank=True, default="India")
    pincode = models.CharField(max_length=20, blank=True, default="")

    # ── Legal / Statutory ─────────────────────────────────────────────
    gst_number = models.CharField(
        max_length=50, blank=True, default="",
        verbose_name="GST Number",
    )
    pan_number = models.CharField(max_length=20, blank=True, default="")
    cin_number = models.CharField(
        max_length=50, blank=True, default="",
        verbose_name="CIN Number",
        help_text="Company Identification Number",
    )
    iec_code = models.CharField(
        max_length=30, blank=True, default="",
        verbose_name="IEC Code",
        help_text="Import Export Code",
    )

    # ── Social Media ──────────────────────────────────────────────────
    website_url = models.URLField(blank=True, default="")
    linkedin_url = models.URLField(blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_url = models.URLField(blank=True, default="")
    instagram_url = models.URLField(blank=True, default="")
    youtube_url = models.URLField(blank=True, default="")
    whatsapp_number = models.CharField(max_length=30, blank=True, default="")

    # ── Other ─────────────────────────────────────────────────────────
    year_established = models.PositiveIntegerField(blank=True, null=True)
    google_maps_embed = models.URLField(
        max_length=1000, blank=True, default="",
        help_text="Google Maps embed URL only (e.g. https://www.google.com/maps/embed?pb=…). Do NOT paste full iframe HTML.",
    )

    @property
    def safe_google_maps_iframe(self):
        """Return sanitised iframe HTML, or empty string if no URL set."""
        from django.utils.html import format_html
        url = (self.google_maps_embed or "").strip()
        if not url:
            return ""
        # Only allow Google Maps origins
        allowed_prefixes = (
            "https://www.google.com/maps/",
            "https://maps.google.com/",
            "https://www.google.com/maps?",
        )
        if not url.startswith(allowed_prefixes):
            return ""
        return format_html(
            '<iframe src="{}" width="100%" height="350" style="border:0;border-radius:12px;"'
            ' allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
            url,
        )

    class Meta:
        verbose_name = "Company Details"
        verbose_name_plural = "Company Details"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        """Ensure only one instance exists (singleton pattern)."""
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        """Return the singleton instance, creating it if needed."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
