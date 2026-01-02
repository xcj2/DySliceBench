N, A, B, C, D = map(int, input().split())
 
S = input()
 
S = S + '#'
 
def continuous_rock_search(S, A, B, C, D):
    begin = min(A, B)
    target = max(C, D)
    for i in range(begin, target - 1):
        if S[i] == '#' and S[i+1] == '#':
            return True
    return False
  
def validation_funuke_move(S, B, D):
    '''
    ふぬけ君が両隣に岩がなくなるまで移動したとき、Dより向こうにはイカないことを確認する。
    True/False and ふぬけの移動後の位置
    '''
    funuke_position = B
    while (B <= D):
        if (S[B-2] == '#' or S[B] == '#'):
            if S[B] == '.' :
                B = B + 1
            else:
                B = B + 2
        elif (S[B-2] == '.' and S[B] == '.'):
            return True, B
    
    return False, -1
  
def KenKenRace(S, A, B, C, D):
    if continuous_rock_search(S, A, B, C, D):
        return False
    
    if C < D:
        return True
    
    if D < C:
        valid , _ = validation_funuke_move(S, B, D)
        if valid:
            return True
        else:
            return False
          
if KenKenRace(S, A, B, C, D):
    print('Yes')
else:
    print('No')
