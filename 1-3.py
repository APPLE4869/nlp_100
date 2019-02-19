# -*- coding: utf-8 -*-
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

TEXT = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

array = re.split(r'\s|\,|\.', TEXT)
array = [a for a in array if a != '']

l = dict()
for a in array:
    if a in l:
        continue
    l[a] = array.count(a)   

print(l)
