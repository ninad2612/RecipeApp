from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = '/login/')
def recipes(request):
    if request.method == "POST":
        
        data = request.POST
        recipename = data.get('recipename')
        recipedescription = data.get('recipedescription')
        recipeimage = request.FILES.get('recipeimage')

        print(recipename)
        print(recipedescription)
        print(recipeimage)

        Recipe.objects.create(
            recipe_name=recipename,
            recipe_description=recipedescription,
            recipe_image=recipeimage,
            
            
        )


        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    context = {'recipes' : queryset}

    return render(request, 'recipes.html')


@login_required(login_url = '/login/')
def display_recipes(request):
   
    queryset = Recipe.objects.all()
    
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipes' : queryset}

    return render(request,'display_recipe.html',context)

def delete_recipe(request,id):

    queryset = Recipe.objects.get(id=id)
    queryset.delete()


    return redirect('/display_recipes/')

def update_recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe':recipe}

    if request.method == "POST":
        
        data = request.POST
        recipename = data.get('recipename')
        recipedescription = data.get('recipedescription')
        recipeimage = request.FILES.get('recipeimage')

        recipe.recipe_name = recipename
        recipe.recipe_description = recipedescription
            
        if recipeimage :    
            recipe.recipe_image = recipeimage

        recipe.save()
        return redirect('/display_recipes/')

    return render(request,'update_recipe.html',context)

