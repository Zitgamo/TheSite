from django.contrib import admin
from firstapp.models import Topic, Webpage, Content,Category, Course, Ckeditor
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Content)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Ckeditor)