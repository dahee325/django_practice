from django.shortcuts import render

# Create your views here.

def profile(request, username, userage):
    context = {
        'username': username,
        'userage': userage,
    }
    return render(request, 'profile.html', context)