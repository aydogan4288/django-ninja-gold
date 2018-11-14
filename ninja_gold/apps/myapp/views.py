from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    try:
        request.session['total']
    except KeyError as e:
        print(e)
        request.session['total'] = 0
    
    if 'message' not in request.session:
        request.session['message']=[]
    return render(request, 'myapp/index.html')
    
def process(request):
    temp_list = request.session['message']
    num = 0
    if request.POST['building'] == 'farm':
        num = random.randint(10,20)
        request.session['total'] += num
        print('*'*50)
        print('farm clicked')
        print('*'*50)
        temp_list.append({"message":'You earned ' + str(num) + ' gold from the farm! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
    if request.POST['building'] == 'cave':
        num = random.randint(5,10)
        request.session['total'] += num
        print('*'*50)
        print('cave clicked')
        print('*'*50)
        temp_list.append({"message":'You earned ' + str(num) + ' gold from the cave! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
    if request.POST['building'] == 'house':
        num = random.randint(2,5)
        request.session['total'] += num
        print('*'*50)
        print('house clicked')
        print('*'*50)
        temp_list.append({"message":'You earned ' + str(num) + ' gold from the house! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
    if request.POST['building'] == 'casino':
        winOrLose = random.randint(0,1)
        if winOrLose == 1:
            num = random.randint(0,50)
            request.session['total'] += num
            temp_list.append({"message":'You earned ' + str(num) + ' gold from the casino! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
        else:
            winOrLose == 0
            num = random.randint(-50,0)
            request.session['total'] += num
            temp_list.append({"message":'You lost ' + str(num) + ' gold at the casino! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())})
    return redirect('/')
    

def reset(request):
    request.session.clear()
    return redirect('/')