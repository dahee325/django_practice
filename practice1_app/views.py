import random
from django.shortcuts import render
from faker import Faker
# Create your views here.

def profile(request, username, userage):
    context = {
        'username': username,
        'userage': userage,
    }
    return render(request, 'profile.html', context)

def godme(request, username):
    feelings = [
        '엉뚱함',
        '잘생김',
        '예쁨',
        '똑똑함',
        '멍청함',
        '배려심',
        '운동신경',
        '먹보',
        '게으름',
        '욕심쟁이',
        '외로움',
        '겁쟁이',
        '인기쟁이',
        '부끄럼',
        '매너',
        '진지함',
    ]
    feel = random.sample(feelings, 3)
    first_feel = feel[0]
    second_feel = feel[1]
    third_feel = feel[2]

    context = {
        'username': username,
        'first_feel': first_feel,
        'second_feel': second_feel,
        'third_feel' : third_feel,
    }
    return render(request, 'godme.html', context)

def godme2(request, username):
    feelings = [
        '엉뚱함',
        '잘생김',
        '예쁨',
        '똑똑함',
        '멍청함',
        '배려심',
        '운동신경',
        '먹보',
        '게으름',
        '욕심쟁이',
        '외로움',
        '겁쟁이',
        '인기쟁이',
        '부끄럼',
        '매너',
        '진지함',
    ]
    feelings = random.sample(feelings, 3)
    
    context = {
        'username': username,
        'feelings': feelings,
    }
    return render(request, 'godme2.html', context)

def words(request):
    fake = Faker()
    fake_words = []

    for i in range(100):
        fake_words.append(fake.words())

    context = {
        'fake_words': fake_words
    }
    return render(request, 'words.html', context)