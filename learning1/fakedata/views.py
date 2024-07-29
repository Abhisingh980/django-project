from django.shortcuts import render
from faker import Faker
from .models import fakedata
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.


def fakedatageneration(request):
    #generate_data(10)

    if request.method == "POST":
        filter_search = request.POST.get('search')
        if filter_search:
            filter_data(filter_search)




    # below code is for generating pagenator

    get_all_data = fakedata.objects.all()
    paginator = Paginator(get_all_data, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    total_pages = paginator.num_pages


    return render(request, 'fake.html', {'data': get_all_data, 'page_obj': page_obj, 'total_pages': total_pages})


def filter_data(request):
    pass



# below code is for generating fake data


def generate_data(n,country=None,option=None):
    fake = Faker()
    for _ in range(n):
        fakedata.objects.create(
            unique_id = fake.random_int(),
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone = fake.phone_number(),
            address = fake.address()
        )

    return "Data Generated Successfully"
