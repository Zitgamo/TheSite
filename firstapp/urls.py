from django.conf.urls import url
from firstapp import views
from django.conf.urls import include
from django.conf.urls.static import static




urlpatterns = [
url(r'^$',views.mainpage, name='mainpage'),
url(r'^webpages.html/$', views.webpages, name='webpages'),
url(r'^contents.html/$', views.contents, name='contents'),
url(r'^homepages.html/$',views.homepages,name='homepages'),
url(r'^homepages/course_detail/(\d+)/$', views.course_detail, name='course_detail'),
]