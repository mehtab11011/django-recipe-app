from django.shortcuts import render,redirect
from .models import recipe_model
from django.http import HttpResponse
from django.core.paginator import Paginator

def add_view(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        if name and description:
            data=recipe_model(recipe_name=name,description=description,image=image)
            data.save()
            return redirect("success_page")
        else:
            return render(request,"recipe_app/home_page.html")
        
        
        
    return render(request,'recipe_app/add_recipe.html')



def success_page(request):
    return render(request,"recipe_app/success_page.html")

def view_recipe_page(request):
    data=recipe_model.objects.all().order_by("-id")
    if request.method=="GET":
        
       st=request.GET.get("recipe_name")
       if st:
        data=recipe_model.objects.filter(recipe_name__icontains=st)
        
    return render(request,"recipe_app/view_recipe_page.html",{"get_all": data})

def detail_page(request,pk):
    try:
        data=recipe_model.objects.get(pk=pk)
    except recipe_model.DoesNotExist:
        return HttpResponse("error",status=404)
    
    return render(request,"recipe_app/recipe_detail.html",{"data":data})



def home_page(request):
    return render(request,"recipe_app/home_page.html")