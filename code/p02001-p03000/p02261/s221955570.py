N = int(input())
S = list(input().split())

def bubble(S):
    sorted_l = []
    un_sorted_l = S[:]
    counter = 0
    while un_sorted_l:
        n = len(un_sorted_l)
        for i in reversed(range(1, n)):
            if un_sorted_l[i-1][1:] <= un_sorted_l[i][1:]:
                continue
            else:
                counter += 1
                un_sorted_l[i-1], un_sorted_l[i] = un_sorted_l[i], un_sorted_l[i-1]
        sorted_l.append(un_sorted_l[0])
        un_sorted_l = un_sorted_l[1:]

    return sorted_l
    
def select(S):
    selection_sort = S[:]
    counter = 0
    for i in range(len(selection_sort)):
        v = selection_sort[i]
        min_v = v
        min_i = i
        for j in range(i, len(selection_sort)):
            if min_v[1:] > selection_sort[j][1:]:
                min_v = selection_sort[j]
                min_i = j
        if v != min_v:
            counter += 1
            selection_sort[i], selection_sort[min_i] = selection_sort[min_i], selection_sort[i]
            
    return selection_sort

def check(X, S):
    d = {}
    for i, s in enumerate(S):
        d[s] = i
        
    for x, y in zip(X[:-1],X[1:]):
        if x[1:] == y[1:] and d[x] > d[y]:
            return 'Not stable'
    
    return 'Stable'
        
        

b = bubble(S)
print(' '.join(b))
print(check(b, S))

s = select(S)
print(' '.join(s))
print(check(s, S))


    
