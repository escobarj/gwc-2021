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


def count(request):
    context = {'nav_count': 'active'}
    return render(request, 'gwc/count.html', context)


def result(request):
    context = {'nav_count': 'active'}

    name = request.POST['name']
    context['name'] = name

    fulltext = request.POST['fulltext']
    words = fulltext.split()
    word_count = len(words)

    context['fulltext'] = fulltext
    context['word_count'] = word_count

    return render(request, 'gwc/result.html', context)


def events(request):
    context = {'nav_events': 'active'}
    return render(request, 'gwc/events.html', context)


def puzzles(request):
    context = {'nav_puzzles': 'active'}
    return render(request, 'gwc/puzzles.html', context)


def resources(request):
    context = {'nav_resources': 'active'}
    return render (request, 'gwc/resources.html', context)


def demo(request):
    context = {'nav_demo': 'active'}
    return render(request, 'gwc/demo.html', context)
