def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

S= one_str()

Q = one_int()

Qs = [ input() for i in range(Q)]
def ss(S, Qs):
    is_not_ac=False
    head = ""
    tail = ""
    for temp in Qs:
#         temp = input()
        if len(temp)>=2:
            T, F, C = temp.split()
            if F=="1":
                if is_not_ac:
                    tail += C
                else:
                    head += C
            else:
                if is_not_ac:
                    head += C
                else:
                    tail += C
        else:        
            is_not_ac = not is_not_ac
    if is_not_ac:
        return tail[::-1] + S[::-1] + head
    else:
        return head[::-1] + S + tail


print(ss(S,Qs))