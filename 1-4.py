# -*- coding: utf-8 -*-
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．

import re, itertools

TEXT = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

splitted = re.split(r'\s|\,|\.', TEXT)
splitted = [s for s in splitted if s != '']
target = [1, 5, 6, 7, 8, 9, 15, 16, 19]
target = [t - 1 for t in target]
first = { splitted[t][0]: t+1 for t in target }
second = { s[0:2]: splitted.index(s)+1 for s in splitted if splitted.index(s) not in target }
print(dict(first, **second))
