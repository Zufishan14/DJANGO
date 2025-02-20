from django.shortcuts import render


rooms = [
    {'id':1, 'name':'Lets Learn Django!'},
    {'id':2, 'name':'Lets learn Python!'},
    {'id':3, 'name':'Lets begin with DevOps!'},
]




def home(request):
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)
def room(request):
    return render(request, 'base/room.html')