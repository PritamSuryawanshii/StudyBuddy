from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Room, Topic
from django.db.models import Q
from .forms import RoomForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.

# rooms = [
#     {'id': 1, 'name': "Let's Learn Python!"},
#     {'id': 2, 'name': "Let's Learn Java!"},
#     {'id': 3, 'name': "Let's Learn JavaScript!"},
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q (topic__name__icontains=q,) |
        Q (name__icontains=q) |
        Q (description__icontains=q)
        )
    
    topics = Topic.objects.all()

    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk): 
    #pk (primary key)
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form =RoomForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)



@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if room.host != request.user:
        return HttpResponse('You do not have permission to modify the room')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) 
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)



@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if room.host != request.user:
        return HttpResponse('you do not have permission to delete the room')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})



def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        # if not, return an error message
        # if yes, redirect to home page

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'base/register.html', context)


def logoutView(request):
    logout(request)
    return redirect('home')
