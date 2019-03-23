from django.shortcuts import render
from firstapp.models import Webpage,Content,Topic,Course
    
# Create your views here.
def mainpage(request):
    return render(request,'firstapp/mainpage.htm')

def webpages(request):
    web_list = Webpage.objects.order_by('name')
    web_dict = {"webpages":web_list }
    return render(request,'firstapp/webpages.htm',context=web_dict)

def contents(request):
    content_list = Content.objects.order_by('name')
    content_dict = {"contents":content_list }
    return render(request,'firstapp/contents.htm',context=content_dict)

def homepages(request):
    course_list_ltv = Course.objects.filter(category = 1).order_by('name')
    part = int(len(course_list_ltv)/2)
    # lst1 = []
    # for i in range(0, part, 1):
    #     lst1.append(course_list_ltv[i])
    # lst2 = []
    # for i in range(part, len(course_list_ltv), 1):
    #     lst2.append(course_list_ltv[i])
    # course_list_cd = Course.objects.filter(category = 2).order_by('name')
    # part2 = int(len(course_list_cd)/2)
    # lst3 = []
    # for i in range(0, part2, 1):
    #     lst3.append(course_list_cd[i])
    # lst4 = []
    # for i in range(part2, len(course_list_cd), 1):
    #     lst4.append(course_list_cd[i])
    # course_dict = {"courses":course_list_ltv,
    #                "courses_cd": course_list_cd,
    #                "course1" :lst1,
    #                "course2":lst2,
    #                "course3" :lst3,
    #                "course4":lst4
    #                }
    # print(course_dict)
    return render(request, "firstapp/homepages.htm", course_list_ltv)
    
def course_detail(request, id=None):
        course = Course.objects.get(pk=id)
        return render(request, "firstapp/course_detail.html", context ={"course":course})