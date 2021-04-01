from django.shortcuts import render
import requests
import json



def homepage(request):
    context = {'nav_home': 'active'}
    return render(request, 'gwc/home.html', context)



def joke(request):
    joke_url = 'https://icanhazdadjoke.com/'
    response = requests.get(joke_url, headers={'Accept': 'application/json'})
    context = response.json()
    context['nav_joke'] = 'active'
    return render(request, 'gwc/joke.html', context)

