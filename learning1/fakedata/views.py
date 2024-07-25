from django.shortcuts import render
from faker import Faker

# Create your views here.
#
def fakedatageneration(request):
    return render(request, 'fake.html')

# def data_from_drop_dawn(request):
#     if request.method == 'POST':
#         selct_value= []
#         option_value = request.POST.get('option_key')

#         for i in range(0, int(option_value)):
#             selct_value.append(i)

#         print(selct_value)
#     return render(request, 'fake.html')


def generate_data(n=10):
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
        fakedata.save()

    return "Data Generated Successfully"
