def multi(a, b) :
    if a == 0 :
        return 0
    elif a == 1 :
        if b == 0 :
            return 0
        else :
            return 1
    else :
        return b

def add(a, b) :
    if a == 0 :
        return b
    elif a == 1 :
        if b == 2 :
            return 2
        else :
            return 1
    else :
        return 2

def minus(a) :
    return (2 - a)

def calc(l) : # '('、')'のない計算式
    l = list(l)
    
    #'-'を計算
    i = len(l)-1
    while True :
        if i < 0 :
            break
        if l[i] == '-' :
            print
            l[i] = str(minus(int(l[i+1])))
            del l[i+1]
        i -= 1 
        
    #'*'を計算
    i = 0
    while True :
        if i >= len(l) :
            break
        if l[i] == '*' :
            l[i-1] = str(multi(int(l[i-1]), int(l[i+1])))
            del l[i:i+2]
        else :
            i += 1
    
    #'+'を計算
    i = 0
    while True :
        if i >= len(l) :
            break
        if l[i] == '+' :
            l[i-1] = str(add(int(l[i-1]), int(l[i+1])))
            del l[i:i+2]
        else :
            i += 1
    return ''.join(l)
    

        
            
def main(l) :
    l = list(l)
    while '(' in l :
        for i in range(len(l)) :
            if l[i] == '(' :
                start = i
            elif l[i] == ')' :
                A = ''.join(l[start+1:i])
                del l[start:i+1]
                l.insert(start, calc(A))
                break
    if len(l) != 1 :
        l = calc(l)
    return ''.join(l)

while True :
    input_l = input()
    if input_l == '.' :
        break
    
    cnt = 0
    for p in ['0', '1', '2'] :
        for q in ['0', '1', '2'] :
            for r in ['0', '1', '2'] :
                l = input_l
                if 'P' in l :
                    l = l.replace('P', p)
                if 'Q' in l :
                    l = l.replace('Q', q)
                if 'R' in l :
                    l = l.replace('R', r)
                if main(l) == '2' :
                    cnt += 1
    print(cnt)
    

