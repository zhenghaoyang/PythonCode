# --coding: utf-8 --
def break_words(stuff):
    words = stuff.split(' ')
    return words 

def sort_words(words):
    """ This function will break up words for us"""
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print word

def print_last_word(words):
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
        
#加分题
'''
ex25.print_first_word(words)
ex25.print_last_word(words)
打印出句子的第一个或最后一个词

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
打印出排序后的句子的第一个或最后一个词

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)

打印出未排序和排完序的句子的第一个词和最后一个词
'''

