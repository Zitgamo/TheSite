from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<H1 ALIGN=CENTER><em>Chào mừng bạn đến với TheSite</em></H1>")

