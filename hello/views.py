import re
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Game, Guess, Chat
import json 
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError

#get popular words and load words list
nltk.download("popular")


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def start_game(request):
    g = Game()
    g.save();
    return HttpResponse('{"game_id": ' + str(Game.objects.last().game_id) + '}');

def submit_guess(request):
    try: 
        g = request.GET.get('guess', None)
        game_id = request.GET.get('game_id', None)
        guess = Guess(guess=g, game=Game.objects.get(game_id=game_id))
        syn_guess = wn.synset(g + ".n.01")
        syn_key = wn.synset(Game.objects.get(game_id=game_id).key_word + ".n.01")
        guess.closest = syn_guess.lowest_common_hypernyms(syn_key)[0].name()[:-5]
        if (guess.closest == g):
            game = Game.objects.get(game_id=game_id)
            game.finished = True
            game.winner = request.GET.get("username", None)
            game.save();
        guess.save();
        return HttpResponse('{"closest": "' + Guess.objects.last().closest + '"}');
    except WordNetError:
        return HttpResponse('{"error": "Word not found"}');

def submit_chat(request):
    try: 
        msg = request.GET.get('message', None)
        game_id = request.GET.get('game_id', None)
        author = request.GET.get('author', None)
        c = Chat(author=author, game=Game.objects.get(game_id=game_id), message=msg)
        c.save();
        return HttpResponse('{"chat": "success"}');
    except WordNetError:
        return HttpResponse('{"error": "chat failed"}');

def update_guesses(request):
    game_id = request.GET.get('game_id', None)
    game = Game.objects.get(game_id=game_id)
    guesses = Guess.objects.filter(game=game)
    guess_dict = {}
    for guess in guesses:
        guess_dict[guess.guess] = guess.closest
    return HttpResponse(json.dumps(guess_dict));

def update_chat(request):
    game_id = request.GET.get('game_id', None)
    game = Game.objects.get(game_id=game_id)
    chats = Chat.objects.filter(game=game)
    chat_dict = {}
    for chat in chats:
        chat_dict[chat.chat_id] = [chat.author, chat.message]
    return HttpResponse(json.dumps(chat_dict));

def game_status(request):
    game_id = request.GET.get('game_id', None)
    fin = Game.objects.get(game_id=game_id).finished
    print(str(game_id) + ": " + str(fin))
    answer = Game.objects.get(game_id=game_id).key_word
    winner = Game.objects.get(game_id=game_id).winner
    if not fin:
        return HttpResponse('{"game_id": "' + game_id + '", "finished": false}');
    else:
        return HttpResponse('{"game_id": "' + game_id + '", "finished": true, "answer": "' + answer + '", "winner": "' + winner +'"}');


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
