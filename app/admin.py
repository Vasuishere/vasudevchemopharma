from django.contrib import admin
from .models import (
    ProductCategory, Product, ProductSpec,
    ProductImage, ProductDocument, ProductFAQ, ProductPricingTier,
    CompanyDetails,
)


# ── Inlines ───────────────────────────────────────────────────────────

class ProductSpecInline(admin.TabularInline):
    model = ProductSpec
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "alt_text", "is_primary", "order")


class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument
    extra = 1
    fields = ("title", "doc_type", "file", "order")


class ProductFAQInline(admin.StackedInline):
    model = ProductFAQ
    extra = 0
    fields = ("question", "answer", "order")


class ProductPricingTierInline(admin.TabularInline):
    model = ProductPricingTier
    extra = 0
    fields = ("min_quantity", "max_quantity", "price_info", "order")


# ── Product Admin ─────────────────────────────────────────────────────

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "sku", "cas_number", "order")
    list_filter = ("category",)
    list_editable = ("order",)
    search_fields = ("name", "description", "sku", "cas_number", "brand_name")
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = [
        ("Basic Information", {
            "fields": (
                "category", "name", "slug", "icon", "brand_name",
                "manufacturer", "description", "full_description",
                "sku", "cas_number", "hs_code", "pack_sizes",
                "country_of_origin", "order",
            ),
        }),
        ("Chemical Identification", {
            "classes": ("collapse",),
            "fields": (
                "common_names", "molecular_formula", "molecular_weight",
                "structure_image", "purity_grade",
                ("is_technical_grade", "is_industrial_grade",
                 "is_analytical_grade", "is_pharma_grade"),
                "un_number",
            ),
        }),
        ("Safety & Regulatory", {
            "classes": ("collapse",),
            "fields": (
                "ghs_classification", "hazard_statements",
                "precautionary_statements", "hazard_pictograms",
                "signal_word", "sds_file",
                "transport_class", "packing_group", "flash_point",
                "storage_conditions", "handling_instructions",
                "disposal_information", "regulatory_compliance",
                "iso_certification",
            ),
        }),
        ("Physical & Chemical Properties", {
            "classes": ("collapse",),
            "fields": (
                "appearance", "odor", "density",
                "melting_point", "boiling_point", "solubility",
                "ph_value", "vapor_pressure", "viscosity",
                "refractive_index", "stability_reactivity",
            ),
        }),
        ("Application & Usage", {
            "classes": ("collapse",),
            "fields": (
                "primary_applications", "industry_usage",
                "recommended_dosage", "compatible_materials", "shelf_life",
            ),
        }),
        ("Packaging & Logistics", {
            "classes": ("collapse",),
            "fields": (
                "net_weight", "gross_weight", "packaging_type",
                "dimensions", "moq", "lead_time",
                "shipping_restrictions", "dangerous_goods",
            ),
        }),
        ("Commercial", {
            "classes": ("collapse",),
            "fields": (
                "customer_support_contact",
                "batch_traceability",
            ),
        }),
    ]

    inlines = [
        ProductSpecInline,
        ProductImageInline,
        ProductDocumentInline,
        ProductFAQInline,
        ProductPricingTierInline,
    ]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("label", "slug", "show_in_overview", "order")
    prepopulated_fields = {"slug": ("label",)}


@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    """Singleton admin — always edit the single company record."""

    fieldsets = [
        ("Branding", {
            "fields": (
                "company_name", "company_logo", "company_name_image",
                "tagline", "about_short",
            ),
        }),
        ("Phone Numbers", {
            "fields": ("phone_primary", "phone_secondary", "phone_export"),
        }),
        ("Email Addresses", {
            "fields": ("email_general", "email_sales", "email_export", "email_support"),
        }),
        ("Address", {
            "fields": (
                "address_line1", "address_line2",
                "city", "state", "country", "pincode",
            ),
        }),
        ("Legal / Statutory", {
            "classes": ("collapse",),
            "fields": ("gst_number", "pan_number", "cin_number", "iec_code"),
        }),
        ("Social Media & Web", {
            "classes": ("collapse",),
            "fields": (
                "website_url", "linkedin_url", "facebook_url",
                "twitter_url", "instagram_url", "youtube_url",
                "whatsapp_number",
            ),
        }),
        ("Other", {
            "classes": ("collapse",),
            "fields": ("year_established", "google_maps_embed"),
        }),
    ]

    def has_add_permission(self, request):
        """Only allow one record."""
        return not CompanyDetails.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
