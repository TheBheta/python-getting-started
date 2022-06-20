import random
words = ["apple", "house", "mouse", "dog", "basketball", "Canada", "cheetah", "pizza", "horse", "pencil", "tree", "sky", "cloud", "earth", "shirt"]

def get_word():
    return words[random.randint(0, len(words) - 1)]

