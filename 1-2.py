# -*- coding: utf-8 -*-
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

STR1 = "パトカー"
STR2 = "タクシー"

index = max([len(STR1), len(STR2)])

result = ""
for i in range(index):
    if (len(STR1) > i):
        result += STR1[i]
    if (len(STR2) > i):
        result += STR2[i]
print(result)
