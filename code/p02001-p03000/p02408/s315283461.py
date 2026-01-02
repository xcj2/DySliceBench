def make_dict_trump():
    t = {}
    for i in range(13):
        t[i+1] = 0
    return t

S = make_dict_trump()
H = make_dict_trump()
C = make_dict_trump()
D = make_dict_trump()

def countup_trump(trump, number):
    trump[number] += 1
    return trump

n = int(input())

for i in range(n):
    kind, number = input().split()
    number = int(number)
    if kind=="S":
        S = countup_trump(S, number)
    elif kind=="H":
        H = countup_trump(H, number)
    elif kind=="C":
        C = countup_trump(C, number)
    elif kind=="D":
        D = countup_trump(D, number)

def output(kind, trump):
    keys = [k for k, v in trump.items() if v == 0]
    for key in keys:
        print(kind, key)

output("S", S)
output("H", H)
output("C", C)
output("D", D)
