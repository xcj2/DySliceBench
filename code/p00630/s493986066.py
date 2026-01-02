def Upper(s) :
    New = []
    i = 0
    while True :
        if i == 0 :
            New.append(s[i].upper())
        elif s[i] == "_" :
            i += 1
            New.append(s[i].upper())
        elif 65 <= ord(s[i]) <= 90 :
            New.append(s[i].upper())
        else :
            New.append(s[i].lower())
        i += 1
        if i >= len(s) :
            break
    return New

def Lower(s) :
    New = []
    i = 0
    while True :
        if s[i] == "_" :
            i += 1
            New.append(s[i].upper())
        elif 65 <= ord(s[i]) <= 90 and i != 0:
            New.append(s[i].upper())
        else :
            New.append(s[i].lower())
        i += 1
        if i >= len(s) :
            break
    return New

def Under_Score(s) :
    New = []
    i = 0
    while True :
        if 65 <= ord(s[i]) <= 90 and i != 0:
            New.append("_")
            New.append(s[i].lower())
        else :
            New.append(s[i].lower())
        i += 1
        if i >= len(s) :
            break
    return New

while True :
    l, x = map(str, input().split())
    if x == "X" :
        break
    
    elif x == "U" :
        print(*Upper(l), sep="")
    elif x == "L" :
        print(*Lower(l), sep="")
    elif x == "D" :
        print(*Under_Score(l), sep="")
        
            
