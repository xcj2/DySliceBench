N = int(input()) 
hs = list(map(int,input().split()))


def minus(x,y): 
    if x > 0:
        return(x - y) 
    else:
        return(x)

def non_zero_min(hs):
    hmin = 1000000 
    for h in hs: 
        if h > 0: 
            if h < hmin: 
                hmin = h 
    return(hmin)


def zero_div_counter(hs):
    length = 0
    n_div = 0
    for i in range(len(hs)):
        h = hs[i]
        if h > 0:
            length += 1
        elif h == 0:
            if length > 0:
                n_div += 1
                length = 0
            else:
                length = 0  
        if i == len(hs)-1:
            if length > 0:
                n_div += 1
    return(n_div)

count = 0

orig_max = max(hs)

for i in range(N):
    # count separation
    n_div = zero_div_counter(hs)
#     print("ndiv: ",n_div)
    nz_min = non_zero_min(hs)
    
    # add count with considering separation
    count += n_div * nz_min
#     print("count:",count)
    
    # update hs
    hs = [minus(x,nz_min) for x in hs] 
#     print("hs  :",hs)

print(count)
