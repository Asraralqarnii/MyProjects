from django.shortcuts import render, redirect
from dojos_ninjas_app.models import Dojo,Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all(),

    }

    return render(request,"index.html",context)



def add_dojo(request):
    if request.method == "POST":
    
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']

        Dojo.objects.create(
            name = name,
            city = city,
            state = state,
            )

    return redirect("/")

def add_ninja(request):
    if request.method == "POST":

        firstname_form = request.POST['first_name']
        lastname_form = request.POST['last_name']
        dojoo = Dojo.objects.get(id= request.POST['dojo_id'])

        Ninja.objects.create(
            first_name = firstname_form,
            last_name = lastname_form,
            dojo = dojoo,
            )

    return redirect("/")
