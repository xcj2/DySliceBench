def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()

A=many_int()

def color_check(num):
    if 1<=num<=399:
        return "hai"
    elif 400<=num<=799:
        return "tya"
    elif 800<=num<=1199:
        return "midori"
    elif 1200<=num<=1599:
        return "mizu"
    elif 1600<=num<=1999:
        return "ao"
    elif 2000<=num<=2399:
        return "ki"
    elif 2400<=num<=2799:
        return "dai"
    elif 2800<=num<=3199:
        return "aka"
    return ""

output = []
overs = 0
for a in A:
    if a >= 3200:
        overs+=1
    else:
        output.append(color_check(a))

cols = len(set(output))
if cols==0:
    cols = 1 
    overs -= 1 
print(cols, cols+overs)