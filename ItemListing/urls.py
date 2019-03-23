from django.conf.urls import url
from ItemListing import views
urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^about.html/$',views.about,name='about'),
url(r'^blog.html/$',views.blog,name='blog'),
url(r'^contact.html/$',views.contact,name='contact'),
url(r'^team.html/$',views.team,name='team'),
]