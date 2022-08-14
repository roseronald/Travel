from django.http import HttpResponse
from django.shortcuts import render


from .models import place
from .models import team

def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'team_result':obj1})
































# Create your views here.
# def demo(request):
#     name="india"
#     return render(request,"homepage.html",{'obj':name})
# def about(request):
#     return render(request,"about.html")