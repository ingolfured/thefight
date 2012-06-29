from movies.models import Movie
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

MAX_INCREASE = 32

def home(request):
    dict = {}
    allmovies = Movie.objects.all().order_by('score').reverse()
    first_movie, second_movie = allmovies.order_by('?')[:2]
    dict['ALL_MOVIES']=allmovies
    dict['FIRST_IMAGE']=first_movie.img_name
    dict['SECOND_IMAGE']=second_movie.img_name
    dict['FIRST_NAME']=first_movie.name
    dict['SECOND_NAME']=second_movie.name
    dict['FIRST_MOVIE_ID']=first_movie.id
    dict['SECOND_MOVIE_ID']=second_movie.id
    return render_to_response('index.html',dict) 

def updateScore(request):
    isFirstWinner = request.POST["isFirstWinner"]
    if isFirstWinner:
        winnerID = request.POST["firstID"]
        loserID = request.POST["secondID"]
    else:
        loserID = request.POST["firstID"]
        winnerID = request.POST["secondID"]

    allmovies = Movie.objects.all().order_by('score').reverse()
    winner = allmovies.get(id=winnerID)
    loser =  allmovies.get(id=loserID)

    winner.score, loser.score = match(winner.score,loser.score)
    winner.won += 1
    loser.lost += 1
    winner.save()
    loser.save()
    
    dict = {}
    first_movie, second_movie = allmovies.order_by('?')[:2]
    dict['FIRST_IMAGE']=first_movie.img_name
    dict['SECOND_IMAGE']=second_movie.img_name
    dict['FIRST_NAME']=first_movie.name
    dict['SECOND_NAME']=second_movie.name
    dict['FIRST_MOVIE_ID']=first_movie.id
    dict['SECOND_MOVIE_ID']=second_movie.id
    return HttpResponse(simplejson.dumps(dict), mimetype="application/x-javascript")


def match(winnerScore, loserScore):
    delta = MAX_INCREASE * 1 / (1 + 10 ** ((winnerScore - loserScore) / 400))
    winnerScore += delta
    loserScore -= delta
    return (winnerScore,loserScore) 
