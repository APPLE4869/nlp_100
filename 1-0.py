# -*- coding: utf-8 -*-
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

STR = "stressed"

# 解１
print(STR[::-1])

# 解２
array = []
for s in STR:
    array.append(s)
array.reverse()
rslt = ""
for a in array:
    rslt += a
print(rslt)
