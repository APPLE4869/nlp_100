# -*- coding: utf-8 -*-
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

import re

TEXT = "I am an NLPer"

def char_bi_gram(text):
    text = text.replace(" ", "")
    length = len(text)
    result = []
    for i in range(length - 1):
        result.append(text[i] + text[i + 1])
    return result

def word_bi_gram(text):
    splitted = re.split(r'\s|\,|\.', text)
    length = len(splitted)
    result = []
    for i in range(length - 1):
        result.append((splitted[i], splitted[i + 1]))
    return result


print(char_bi_gram(TEXT))
print(word_bi_gram(TEXT))
