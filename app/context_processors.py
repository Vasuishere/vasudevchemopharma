from .models import CompanyDetails


def company_details(request):
    """Make company details available in every template as {{ company }}."""
    return {"company": CompanyDetails.load()}
