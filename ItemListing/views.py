from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"ItemListing/index.htm")

def about(request):
    return render(request,"ItemListing/about.htm")

def blog(request):
    return render(request,"ItemListing/blog.htm")

def contact(request):
    return render(request,"ItemListing/contact.htm")

def team(request):
    return render(request,"ItemListing/team.htm")
