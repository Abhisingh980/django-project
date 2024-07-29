from django.shortcuts import render
from faker import Faker
from .models import fakedata
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views import View
from django.db.models import Q

# Create your views here.


class FakeDataView(View):

    def __init__(self) -> None:
        super().__init__()

    def filter_data(self,request,filter_search):
        # filter data from database in all catagory
        if filter_search:
                    filter_query_data = fakedata.objects.filter(
                        Q(first_name__icontains=filter_search) |
                        Q(last_name__icontains=filter_search) |
                        Q(email__icontains=filter_search) |
                        Q(phone__icontains=filter_search) |
                        Q(address__icontains=filter_search)
                    )
        else:
            filter_query_data = fakedata.objects.all()

        return filter_query_data

    def get(self,request):

        get_all_data = fakedata.objects.all()
        paginator = Paginator(get_all_data, 10)  # Show 10 items per page

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        total_pages = paginator.num_pages

        context = {'data': get_all_data, 'page_obj': page_obj, 'total_pages': total_pages}
        return render(request, 'fake.html', context)

    def post(self, request):
        filter_search = request.POST.get('search')
        if filter_search:
            filter_query_data = self.filter_data(self,filter_search)
        else:
            filter_query_data = fakedata.objects.all()

        paginator = Paginator(filter_query_data, 10)  # Show 10 items per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        total_pages = paginator.num_pages

        context = {'data': filter_query_data, 'page_obj': page_obj, 'total_pages': total_pages}
        return render(request, 'fake.html', context)






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
