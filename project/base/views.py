from django.shortcuts import render


rooms = [
    {'id':1, 'name':'Lets Learn Django!'},
    {'id':2, 'name':'Lets learn Python!'},
    {'id':3, 'name':'Lets begin with DevOps!'},
]




def home(request):
    return render(request, 'home.html', {'rooms':rooms})
def room(request):
    return render(request, 'room.html')