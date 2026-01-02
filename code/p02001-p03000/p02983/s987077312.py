L, R= list(map(int, input().split()))

def get_amari():
    min_ = 2019
    for i in range(L,R):
        for j in range(i+1, R+1):
            if (i*j)%2019 < min_:
                min_ = (i*j)%2019
    return min_
   
def get_flg3():
    if R-L >= 3:
        return True
    elif R//3 != L//3:
        return True
    else:
        return False
    

def get_flg673():
    if R-L >= 673:
        return True
    elif R//673 != L//673:
        return True
    else:
        return False

if get_flg3() & get_flg673():
    print(0)
else:
    print(get_amari())
