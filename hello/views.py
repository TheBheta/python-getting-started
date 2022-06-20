import re
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Game, Guess, Chat
from .words import get_word
import json 
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError
import random

#get popular words and load words list
nltk.download("book")


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def start_game(request):
    g = Game()
    g.key_word = get_word()
    g.host = request.GET.get("username", None);
    g.save();
    return HttpResponse('{"game_id": ' + str(Game.objects.last().game_id) + '}');

def reset_game(request):
    g = Game.objects.get(game_id=request.GET.get("game_id", None))
    g.finished = False
    g.key_word = get_word()
    g.winner = ""
    g.save()
    Guess.objects.filter(game=g.game_id).delete();
    return HttpResponse('{"game_id": ' + str(Game.objects.last().game_id) + '}');

def submit_guess(request):
    try: 
        g = request.GET.get('guess', None)
        game_id = request.GET.get('game_id', None)
        guess = Guess(guess=g, game=Game.objects.get(game_id=game_id))
        syn_guess = wn.synset(g + ".n.01")
        syn_key = wn.synset(Game.objects.get(game_id=game_id).key_word + ".n.01")
        guess.closest = syn_guess.lowest_common_hypernyms(syn_key)[0].name()[:-5]
        if (guess.closest == syn_key.name()[:-5]):
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

def get_hint(request):
    game_id = request.GET.get('game_id', None)
    game = Game.objects.get(game_id=game_id)
    guess = Guess(guess="hint", game=Game.objects.get(game_id=game_id))
    word = wn.synset(game.key_word + ".n.01")
    hints = word.hypernyms() + word.hyponyms() + word.member_holonyms()
    trueHints = []
    for hint in hints:
        if word.name() not in hint.name():
            trueHints.append(hint.name()[:-5])
    if (len(trueHints) == 0):
        guess.closest = "bro the word " + word + " is just stupid"
    else:
        guess.closest = random.choice(trueHints)
    guess.save();
    return HttpResponse('{"hint": "success"}');

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
    host = Game.objects.get(game_id=game_id).host
    if not fin:
        return HttpResponse('{"game_id": "' + game_id + '", "finished": false, "host": "' + host + '"}');
    else:
        return HttpResponse('{"game_id": "' + game_id + '", "finished": true, "answer": "' + answer + '", "winner": "' + winner +'", "host": "' + host + '"}');


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
