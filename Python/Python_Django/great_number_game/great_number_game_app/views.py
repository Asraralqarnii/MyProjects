from django.shortcuts import render, HttpResponse,redirect
import random 	                

def index(request):
    if 'number' not in request.session: # if key in request session
        request.session['number']= random.randint(1, 100)# create 
    if 'result' not in request.session:
        request.session['result']=""
        #request.session['counter']=1 #create counter

    return render(request,'index.html')

def process_guess(request):
    #request.session['counter']+=1
    guess = int(request.POST['guess'])
    # too high
    if guess > request.session['number']:
        request.session['result'] = 'Too High'
    # too Low
    if guess < int(request.session['number']):
        request.session['result'] = 'Too Low'
    # correct
    if guess == int(request.session['number']):
        request.session['result'] = 'win'
    return render(request,'index.html')

def newgame(request):
    request.session.clear()

    return redirect("/")
