from django.shortcuts import render
from faker import Faker
from .models import fakedata
from django.core.paginator import Paginator

# Create your views here.
#
def fakedatageneration(request):
    #generate_data(10)
    get_all_data = fakedata.objects.all()
    paginator = Paginator(get_all_data, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'fake.html', {'data': get_all_data, 'page_obj': page_obj})

# def data_from_drop_dawn(request):
#     if request.method == 'POST':
#         selct_value= []
#         option_value = request.POST.get('option_key')

#         for i in range(0, int(option_value)):
#             selct_value.append(i)

#         print(selct_value)
#     return render(request, 'fake.html')


def generate_data(n):
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
