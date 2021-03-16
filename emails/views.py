from django.shortcuts import render
from django.http import HttpResponse
from .models import EmailEntry
# Create your views here.


def email_entry_get_view(request, *args, **kwargs):
    obj = EmailEntry.objects.get(id=1)
    return HttpResponse(f"<h1>Hello {obj.email}</h1>")


# def email_entry_list_view():
#
#     return
#
#
# def email_entry_create_view():
#
#     return
#
#
# def email_entry_update_view():
#
#     return
#
#
# def email_entry_destroy_view():
#
#     return
