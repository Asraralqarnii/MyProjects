from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['activities'] =[]
        request.session['color']=""

    return render(request,"index.html")

def process(request):

    if request.method == 'POST':
        data ={
            'text' : '',
            'color' : 'green'


    }
    if request.POST['location'] == "farm":
        gold_amount = random.randint(10,20)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        data['text'] = f"Earned {gold_amount} from farm! ({time}) "
        request.session['gold'] += gold_amount

    elif request.POST['location'] == "cave":
        gold_amount = random.randint(5,10)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        data['text'] = f"Earned {gold_amount} from cave! ({time}) "
        request.session['gold'] += gold_amount

    elif request.POST['location'] == "house":
        gold_amount = random.randint(2,5)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        data['text'] = f"Earned {gold_amount} from house! ({time})"
        request.session['gold'] += gold_amount

    elif request.POST['location'] == "casino":
        gold_amount = random.randint(-50,50)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        if gold_amount > 0:
            data['text'] = f"Earned {gold_amount} from casino! ({time})"
        else:
            postive = abs(gold_amount) 
            data['text'] = f"Entered a casino and lost {postive} golds... Ouch.. ({time})"
            data['color'] = 'red'
    request.session['gold'] += gold_amount



    request.session['activities'].append(data)


    return redirect("/")