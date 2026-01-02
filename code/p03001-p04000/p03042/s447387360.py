#INPUT
#S

#S は長さ 4 の数字列

#長さ 4 の数字列 S が与えられます。
#あなたは、この数字列が以下のフォーマットのどちらであるか気になっています。
#YYMM フォーマット: 西暦年の下 2 桁と、月を 2 桁で表したもの 
#                (例えば 1 月なら 01) をこの順に並べたもの
#MMYY フォーマット: 月を 2 桁で表したもの 
#                (例えば 1 月なら 01) と、西暦年の下 2 桁をこの順に並べたもの
#与えられた数字列のフォーマットとして考えられるものが
#YYMM フォーマットのみである場合 YYMM を、 
#MMYY フォーマットのみである場合 MMYY を、 
#YYMM フォーマット と MMYY フォーマットのどちらの可能性もある場合
#AMBIGUOUS を、 
#どちらの可能性もない場合 NA を出力してください。

#YYMM, MMYY, AMBIGUOUS, NA のうち正しいものを出力せよ。

def isMonth(x):
    num = int(x)
    return (1 <= num and num <= 12)

def isYear(x):
    num = int(x)
    return (0 <= num and num <= 99)

def isYYMM(head, tail):
    return (isYear(head) and isMonth(tail))

def isMMYY(head, tail):
    return (isMonth(head) and isYear(tail))

S = input()
head = S[0:2]
tail = S[2:4]

if (isYYMM(head, tail) and isMMYY(head, tail)):
    res = 'AMBIGUOUS'
elif isYYMM(head, tail):
    res = 'YYMM'
elif isMMYY(head, tail):
    res = 'MMYY'
else:
    res = 'NA'

print(res)

