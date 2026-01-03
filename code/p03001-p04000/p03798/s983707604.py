N = int(input())
s = input()

def sheep_wolf_allocator(given_string ,first_allocate, second_allocate):
    '''
    与えられた文字列を満たすように1...Nまで羊/狼を割り当てる。
    最後にN匹目と1匹目の検証を行う。
    
    引数
    ------------------------------
    given_string: 動物の主張 ooxoxox..
    first_allocate: 1番に割り当てる動物(S/W)
    second_allocate: 2番に割り当てる動物(S/W)
    
    戻り値
    ------------------------------
    検証失敗時 -> -1
    swallocation: 羊/狼の割当結果文字列, 検証失敗時は返さない
    '''
    
    def verse(ws_char):
        if ws_char == "W":
            return "S"
        else:
            return "W"
        
    
    # allocation
    swallocation = []
    swallocation.append(first_allocate)
    swallocation.append(second_allocate)
    
    N = len(given_string)
    
    for pi in range(1, N):
        if swallocation[pi] == 'S':
            if given_string[pi] == 'o':
                swallocation.append(swallocation[pi - 1])
            else:
                swallocation.append(verse(swallocation[pi - 1]))
        else:
            if given_string[pi] == 'o':
                swallocation.append(verse(swallocation[pi - 1]))
            else:
                swallocation.append(swallocation[pi - 1])
    
    # verification
    if swallocation[0] == 'S':
        if given_string[0] == 'o':
            if swallocation[N - 1] != swallocation[1]:
                return -1
        else:
            if swallocation[N - 1] == swallocation[1]:
                return -1
    else:
        if given_string[0] == 'o':
            if swallocation[N - 1] == swallocation[1]:
                return -1
        else:
            if swallocation[N - 1] != swallocation[1]:
                return -1
    
    if swallocation[0] != swallocation[N]:
        return -1
    
    return ''.join(swallocation[:N])
  
def main():
    judge1 = sheep_wolf_allocator(s, "S", "S")
    judge2 = sheep_wolf_allocator(s ,"S", "W")
    judge3 = sheep_wolf_allocator(s ,"W", "S")
    judge4 = sheep_wolf_allocator(s ,"W", "W")
    
    if judge1 != -1:
        print(judge1)
        return
    
    if judge2 != -1:
        print(judge2)
        return
    
    if judge3 != -1:
        print(judge3)
        return
    
    if judge4 != -1:
        print(judge4)
        return
    
    print(-1)
    return
  
main()