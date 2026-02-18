"""
Product catalogue data served to the products page.
Each product is rendered as a card; categories drive the filter nav.
"""

CATEGORIES = [
    {"slug": "all", "label": "All Products"},
    {"slug": "industrial", "label": "Industrial Chemicals"},
    {"slug": "api", "label": "Pharmaceutical API Intermediates"},
    {"slug": "specialty", "label": "Specialty Chemicals"},
]

PRODUCTS = [
    # ── Industrial Chemicals ──────────────────────────────────────────
    {
        "icon": "H2S",
        "category_slug": "industrial",
        "category_label": "Industrial Chemical",
        "name": "MEA Triazine 78% H2S Scavenger",
        "description": (
            "High-purity chemical for oil & gas industry applications, "
            "effectively removing hydrogen sulfide from industrial processes."
        ),
        "specs": [
            {"label": "Purity", "value": "78%"},
            {"label": "Packaging", "value": "200L Drums"},
            {"label": "Application", "value": "Oil & Gas"},
        ],
    },
    {
        "icon": "PTSA",
        "category_slug": "industrial",
        "category_label": "Industrial Chemical",
        "name": "P-toluenesulfonic Acid",
        "description": (
            "High-grade acid used in various industrial applications "
            "including catalysis and chemical synthesis."
        ),
        "specs": [
            {"label": "Purity", "value": "98%"},
            {"label": "Packaging", "value": "PP Bag"},
            {"label": "Grade", "value": "Industrial"},
        ],
    },
    {
        "icon": "CuS",
        "category_slug": "industrial",
        "category_label": "Industrial Chemical",
        "name": "Copper Sulphate",
        "description": (
            "Industrial grade copper sulphate for various applications "
            "including agriculture, water treatment, and chemical processes."
        ),
        "specs": [
            {"label": "Grade", "value": "Industrial"},
            {"label": "Form", "value": "Crystals"},
            {"label": "Application", "value": "Multi-purpose"},
        ],
    },
    {
        "icon": "MnS",
        "category_slug": "industrial",
        "category_label": "Industrial Chemical",
        "name": "Manganese Sulphate",
        "description": (
            "High-quality manganese sulphate for fertilizer production, "
            "animal feed supplements, and industrial applications."
        ),
        "specs": [
            {"label": "Grade", "value": "Industrial/Feed"},
            {"label": "Form", "value": "Powder/Granules"},
            {"label": "Purity", "value": "99%"},
        ],
    },
    # ── Pharmaceutical APIs ───────────────────────────────────────────
    {
        "icon": "ALB",
        "category_slug": "api",
        "category_label": "Pharmaceutical API",
        "name": "Albendazol",
        "description": (
            "Anti-parasitic pharmaceutical active ingredient for treating "
            "various worm infections with high efficacy."
        ),
        "specs": [
            {"label": "Grade", "value": "Pharmaceutical"},
            {"label": "Purity", "value": "USP/BP"},
            {"label": "Category", "value": "Anthelmintic"},
        ],
    },
    {
        "icon": "KTC",
        "category_slug": "api",
        "category_label": "Pharmaceutical API",
        "name": "Ketoconazole",
        "description": (
            "Antifungal API for treating various fungal infections, "
            "available in multiple pharmaceutical grades."
        ),
        "specs": [
            {"label": "CAS Number", "value": "65277-42-1"},
            {"label": "Grade", "value": "IP/BP/USP"},
            {"label": "Category", "value": "Antifungal"},
        ],
    },
    {
        "icon": "PGB",
        "category_slug": "api",
        "category_label": "Pharmaceutical API",
        "name": "Pregabalin",
        "description": (
            "Anti-convulsant medication API used for treating epilepsy, "
            "neuropathic pain, and anxiety disorders."
        ),
        "specs": [
            {"label": "Grade", "value": "Pharmaceutical"},
            {"label": "Purity", "value": "USP"},
            {"label": "Category", "value": "Anticonvulsant"},
        ],
    },
    # ── Specialty Chemicals ───────────────────────────────────────────
    {
        "icon": "BCE",
        "category_slug": "specialty",
        "category_label": "Specialty Chemical",
        "name": "Bis(2-chloroethyl)amine Hydrochloride",
        "description": (
            "High-purity specialty chemical intermediate used in "
            "pharmaceutical synthesis and research applications."
        ),
        "specs": [
            {"label": "Grade", "value": "Research/Pharma"},
            {"label": "Purity", "value": "98%+"},
            {"label": "Application", "value": "Synthesis"},
        ],
    },
    {
        "icon": "DEA",
        "category_slug": "specialty",
        "category_label": "Specialty Chemical",
        "name": "Di Ethyl Amino Ethyl Chloride Hydrochloride",
        "description": (
            "Specialized chemical intermediate for pharmaceutical and "
            "fine chemical synthesis with high purity standards."
        ),
        "specs": [
            {"label": "Grade", "value": "Pharmaceutical"},
            {"label": "Purity", "value": "99%+"},
            {"label": "Form", "value": "Hydrochloride Salt"},
        ],
    },
    {
        "icon": "AMT",
        "category_slug": "specialty",
        "category_label": "Specialty Chemical",
        "name": "2-Amino-5-methylthiazole",
        "description": (
            "Pharmaceutical intermediate used in the synthesis of various "
            "therapeutic compounds and research chemicals."
        ),
        "specs": [
            {"label": "Grade", "value": "Pharmaceutical"},
            {"label": "Purity", "value": "98%"},
            {"label": "Application", "value": "Intermediate"},
        ],
    },
    {
        "icon": "CEH",
        "category_slug": "specialty",
        "category_label": "Specialty Chemical",
        "name": "2-Chloroethylamine Hydrochloride",
        "description": (
            "API intermediate used in pharmaceutical manufacturing and "
            "specialty chemical synthesis processes."
        ),
        "specs": [
            {"label": "Grade", "value": "API Intermediate"},
            {"label": "Purity", "value": "99%"},
            {"label": "Form", "value": "Crystalline"},
        ],
    },
]

PRODUCT_CATEGORIES_OVERVIEW = [
    {
        "icon_class": "bi bi-gear-fill",
        "title": "Industrial Chemicals",
        "description": (
            "High-quality industrial chemicals for oil & gas, "
            "manufacturing, and processing industries"
        ),
    },
    {
        "icon_class": "bi bi-capsule",
        "title": "Pharmaceutical APIs",
        "description": (
            "Active pharmaceutical ingredients meeting international "
            "quality standards for drug manufacturing"
        ),
    },
    {
        "icon_class": "bi bi-flask",
        "title": "Specialty Chemicals",
        "description": (
            "Specialized chemical intermediates and compounds for "
            "pharmaceutical and research applications"
        ),
    },
    {
        "icon_class": "bi bi-heart",
        "title": "Personal Care",
        "description": (
            "Natural and cosmetic grade products for personal care "
            "and skincare applications"
        ),
    },
]

# NOTE: "Personal Care" appears in PRODUCT_CATEGORIES_OVERVIEW for the
# products-page grid but has no matching entries in CATEGORIES or PRODUCTS yet.
# The DB category (slug="personal-care", show_in_overview=True) was seeded
# during the initial data load so the overview card renders correctly.
# Add products via Django Admin when the catalogue expands to Personal Care.
