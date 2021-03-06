from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from customer.models import Customer


def index(request):
    template = loader.get_template('index.html')
    context = {"customers": Customer.objects.all()}
    return HttpResponse(template.render(context, request))