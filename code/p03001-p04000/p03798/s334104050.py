import sys
n = int(input())
s = input()

# ls[i]とls[i-1]の情報からls[i+1]を決定する関数
def decide_right(ls):
    '''
    ls[0]とls[1]が確定したlsを与えられたら、その情報からls全体(一意に定まる)を返す
    '''
    N = len(ls)
    for i in range(1,N-1):
        if ls[i] == 'S':
            if s[i] == 'o':
                ls[i+1] = ls[i-1]
            else:
                if ls[i-1] == 'S':
                    ls[i+1] = 'W'
                else:
                    ls[i+1] = 'S'
        else:
            if s[i] == 'o':
                if ls[i-1] == 'S':
                    ls[i+1] = 'W'
                else:
                    ls[i+1] = 'S'
            else:
                ls[i+1] = ls[i-1]
    return ls

'''
def decide_left(ls):
    #ls[1]とls[0]が確定したlsを与えられたら、その情報からls全体(一意に定まる)を返す
    
    N = len(ls)
    for i in range(N,0,-1):
        if s[i] == 'o':
            ls[i-1] = ls[i+1]
        else:
            if ls[i+1] == 'S':
                ls[i-1] = 'W'
            else:
                ls[i-1] = 'S'
'''

def check(first):
    # 矛盾のないlsを発見し次第それをreturn、可能性が無くなったらFalseをリターン
    # ls1は左から決めていく
    ls1 = [0] * (n+1)
    ls1[0] = first

    for second in ['S','W']:
        ls1[1] = second
        ls1 = decide_right(ls1)
        
        if ls1[0] != ls1[-1]:
            continue
        
        # 0の両隣の判定

        ls = ls1[:-1]
        res = True
        for i in range(n):
            r = i+1
            if r == n:
                r = 0
            if ls[i] == 'S':
                if s[i] == 'o' and ls[i-1] != ls[r]:
                    res = False
                    break
                elif s[i] == 'x' and ls[i-1] == ls[r]:
                    res = False
                    break
            else:
                if s[i] == 'o' and ls[i-1] == ls[r]:
                    res = False
                    break
                elif s[i] == 'x' and ls[i-1] != ls[r]:
                    res = False
                    break
        if not res:
            continue
        '''
        ls2 = [0] * (n+1)
        ls2[-1] = first
        if s[0] == 'o':
            ls2[-2] = second
        else:
            if second == 'S':
                ls2[-2] = 'W'
            else:
                ls2[-2] = 'S'
        ls2 = decide_left(ls2)
        if ls2[0] != ls2[-1]:
            continue
        
        for i in range(n+1):
            if ls1[i] != ls2[i]:
                continue
        '''
        
        return ls1[:-1]
    
    return False

for first in ['S','W']:
    c = check(first)
    if c:
        print(*c,sep='')
        sys.exit()
print(-1)