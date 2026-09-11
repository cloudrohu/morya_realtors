from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Min, Max
from django.contrib import messages

from .models import (
    Project,
    Configuration,
    Gallery,
    RERA_Info,
    BookingOffer,
    Overview,
    USP,
    Amenities,
    Header,
    WelcomeTo,
    Connectivity,
    WhyInvest,
    Enquiry,
    ProjectFAQ,
)



from apps.properties_utility.models import ProjectAmenities, PropertyType
from apps.utility.models.location import Location, LocationType

from apps.core.models.website import Setting

def get_settings():
    """Helper function to fetch settings object safely"""
    return Setting.objects.first()



def index(request):

    projects = Project.objects.filter(
        is_active=True
    ).order_by("project_name")

    # ================= CITY =================
    city_id = request.GET.get("city_id")

    if city_id:
        projects = projects.filter(
            city_id=city_id
        )

    # ================= LOCALITY =================
    locality_id = request.GET.get("locality_id")

    if locality_id:
        try:
            selected_locality = Location.objects.get(
                pk=locality_id,
                location_type=LocationType.LOCALITY_AREA,
            )

            descendant_localities = selected_locality.get_descendants(
                include_self=True
            )

            projects = projects.filter(
                locality__in=descendant_localities
            )

        except Location.DoesNotExist:
            pass

    # ================= CONSTRUCTION STATUS =================
    status = request.GET.get("status")

    if status:
        projects = projects.filter(
            construction_status__iexact=status
        )

    # ================= KEYWORDS =================
    keywords = request.GET.get("keywords", "").strip()

    if keywords:
        projects = projects.filter(
            Q(project_name__icontains=keywords)
            |
            Q(developer__name__icontains=keywords)
        )

    # ================= CITIES =================

    available_cities = Location.objects.filter(
        location_type=LocationType.DISTRICT_CITY
    ).order_by("name")

    # ================= LOCALITIES =================

    available_localities = Location.objects.filter(
        location_type=LocationType.LOCALITY_AREA
    ).order_by("name")

    # ================= AMENITIES =================

    amenities = ProjectAmenities.objects.all()

    # ================= CONSTRUCTION STATUS =================

    construction_statuses = (
        Project.objects
        .exclude(construction_status__isnull=True)
        .exclude(construction_status="")
        .values_list(
            "construction_status",
            flat=True
        )
        .distinct()
        .order_by("construction_status")
    )

    context = {
        "projects": projects,
        "available_cities": available_cities,
        "available_localities": available_localities,
        "amenities": amenities,
        "construction_statuses": construction_statuses,
        "values": request.GET,
    }

    return render(
        request,
        "properties/index.html",
        context
    )

def get_bhk_choices():
    return [
        choice[0]
        for choice in Project.BHK_CHOICES
    ]

def search_suggestions(request):

    q = request.GET.get("q", "").strip()

    results = []

    if q:

        # ================= PROJECTS =================

        projects = Project.objects.filter(
            project_name__icontains=q
        )[:5]

        for p in projects:

            results.append({
                "name": p.project_name,
                "type": "Project",
            })

        # ================= LOCATIONS =================

        locations = Location.objects.filter(
            name__icontains=q,
            location_type__in=[
                LocationType.LOCALITY_AREA,
                LocationType.SUBLOCALITY_AREA,
            ],
        )[:5]

        for location in locations:

            results.append({
                "name": location.name,
                "type": "Locality",
            })

    return JsonResponse(
        results,
        safe=False
    )


def search_projects(request):

    settings_obj = get_settings()

    location = request.GET.get("q", "").strip()
    city = request.GET.get("city", "").strip()
    amenities = request.GET.get("amenities")
    status = request.GET.get("construction_status")
    bhk = request.GET.get("bhk")
    developer_slug = request.GET.get("developer") 
    locality_ids = request.GET.getlist("locality")
    projects = Project.objects.filter(is_active=True)


    # 🔍 Single Clean Search Block
    if location:
        search_term = location.split(",")[0].strip()

        projects = projects.filter(
            Q(project_name__icontains=search_term) |
            Q(locality__title__icontains=search_term) |
            Q(city__name__icontains=search_term) |
            Q(developer__title__icontains=search_term)
        )

    # 🌆 City
    if city:
        projects = projects.filter(city__name__iexact=city)
 

    # 📍 Locality (MPTT)
    if locality_ids:
        selected_localities = Locality.objects.filter(id__in=locality_ids)
        all_localities = Locality.objects.none()
        for loc in selected_localities:
            all_localities |= loc.get_descendants(include_self=True)
        projects = projects.filter(locality__in=all_localities).distinct()

    if developer_slug:
        projects = projects.filter(developer__slug=developer_slug)

    if amenities:
        amenity_list = [a.strip() for a in amenities.split(",") if a.strip()]
        if amenity_list:
            projects = projects.filter(
                project_amenities__amenities__title__in=amenity_list
            ).distinct()

    if status:
        status_list = [s.strip() for s in status.split(",") if s.strip()]
        if status_list:
            projects = projects.filter(construction_status__in=status_list).distinct()

    selected_bhk_list = []
    if bhk:
        selected_bhk_list = [b.strip() for b in bhk.split(",") if b.strip()]
        if selected_bhk_list:
            bhk_query = Q()
            for b in selected_bhk_list:
                bhk_query |= Q(bhk_type__icontains=b) | Q(configurations__bhk_type__icontains=b)
            projects = projects.filter(bhk_query).distinct()

    # ⚡ Optimize + Pagination
        projects = projects.select_related(
            "city",
            "locality",
            "developer"
        ).order_by("-create_at")

    paginator = Paginator(projects, 9)
    projects_page = paginator.get_page(request.GET.get("page"))


    context = {
        "projects": projects_page,

        "amenities": ProjectAmenities.objects.all(),

        "construction_status": (
            Project.objects
            .exclude(construction_status__isnull=True)
            .exclude(construction_status="")
            .values_list("construction_status", flat=True)
            .distinct()
            .order_by("construction_status")
        ),

        "bhk_choices": get_bhk_choices(),

        "selected_amenities": amenities,

        "selected_status": status,

        "selected_bhk": bhk,

        

        "selected_bhk_list": selected_bhk_list,

        "available_localities": Location.objects.filter(
            location_type=LocationType.LOCALITY_AREA
        ).order_by("name"),

        "selected_locality_ids": [
            str(x) for x in locality_ids
        ],
    }

    return render(request, "home/residential_list.html", context)




def residential_projects(request):


    settings_obj = get_settings()


    projects = (
        Project.objects
        .filter(is_active=True)
        .annotate(
            min_price=Min(
                "configurations__price_in_rupees"
            ),
            max_price=Max(
                "configurations__price_in_rupees"
            ),
        )
    )

    context = {
        "projects": projects,
        "page_title": "Residential Projects",
        'settings_obj': settings_obj,
        
    }

    return render(request,"home/residential_list.html",context,)



def commercial_projects(request):

    projects = Project.objects.filter(is_active=True)

    context = {
        "projects": projects,
        "page_title": "Commercial Projects",
    }

    return render(request,"projects/commercial_list.html",context,)

def project_details(request, id, slug):

    project = get_object_or_404(Project,id=id,slug=slug,is_active=True)

    carpet_range = (
        project.configurations.aggregate(
            min_area=Min("area_sqft"),
            max_area=Max("area_sqft"),
        )
    )

    related_projects = (
        Project.objects.filter(
            city=project.city,
            is_active=True
        )
        .exclude(id=project.id)[:8]
    )

    context = {
        "project": project,
        "min_carpet": carpet_range["min_area"],
        "max_carpet": carpet_range["max_area"],
        "related_projects": related_projects,
    }

    return render(request,"projects/project_detail.html",context,)

def submit_enquiry(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    if request.method == "POST":

        Enquiry.objects.create(
            project=project,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )

        messages.success(
            request,
            "Enquiry Submitted Successfully"
        )

        return redirect("thank_you")

    return redirect(
        "project_details",
        id=project.id,
        slug=project.slug,
    )

def thank_you(request):
    return render(
        request,
        "projects/thank_you.html"
    )