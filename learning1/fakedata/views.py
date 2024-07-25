from django.shortcuts import render

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
