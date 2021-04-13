
import pickle
import logging
import itertools

WORDS = open('play/google-books-common-words.txt')

LEER = WORDS.read()


def is_subset(word, choices):
    _choices = list(choices)
    for c in word:
        if c not in _choices:
            return False
        _choices.remove(c)
    return True


def get_words(length, letters):
    length = int(length)
    candidates = []
    selected = []

    for key, value in WORDS.items():
        if len(key) == length:
            candidates.append(key)
    for word in candidates:
        if is_subset(word, letters):
            selected.append(word)
    logging.info('Got {0} matches with length of {1} where choices {2}'.format(
        len(selected), length, letters))
    return selected


def get_palabras_dic(length, letters):
    length = int(length)
    candidates = []
    selected = {}

    print('DDDDDDDDDDDDDDDDDDDDDDDDD', WORDS)

    dicionario = dict()


    f = open("combinations.txt",'w')
    lista = list(itertools.permutations(letters, int(length)))

    for i in lista: 
        print(i)
        dicionario[lista[i]] = dicionario.get(lista[i], 0) +1

    print(dicionario)


    for key, value in WORDS.items():
        if len(key) == length:
            candidates.append(key)
    for word in candidates:
        if is_subset(word, letters):
            selected.update({word: WORDS.get(word)})
    logging.info('Got {0} matches with length of {1} where choices {2}'.format(
        len(selected.keys()), length, letters))
    return selected