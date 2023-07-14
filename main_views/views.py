from django.shortcuts import render


# Create your views here.

def views_home(request):
    return render(request, 'Home.html')


def views_info(request):
    return render(request, 'info.html')


def views_contacts(request):
    return render(request, 'Contacts.html')
