word = input()

n = len(word)

a = (n-1)//2
b = (n+3)//2

word2 = word[:a]
word3 = word[b-1:]

def kai1():
    for i in range(a):
        if(word[i] != word[-1*(i+1)]):
            return False
    return True
def kai2():
    wl = len(word2)
    if(wl % 2 == 0):
        wl = wl//2
    else:
        wl = (wl-1)//2
    for i in range(wl):
        if(word2[i] != word2[-1*(i+1)]):
            return False
    return True
def kai3():

    wl = len(word3)
    if(wl % 2 == 0):
        wl = wl//2
    else:
        wl = (wl-1)//2
    for i in range(wl):
        if(word3[i] != word3[(-1*(i+1))]):
            return False
    return True

if(kai1() and kai2() and kai3()):
    print("Yes")
else:
    print("No")
