from crc.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    return render_to_response('index.html')