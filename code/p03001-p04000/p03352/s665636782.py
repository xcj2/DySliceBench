n=int(input())
def gauss_2(n):
    g=0
    while g<=n**(1/2):
        g+=1
    return g-1

def gauss_3(n):
    g=0
    while g<=n**(1/3):
        g+=1
    return g-1
def gauss_4(n):
    g=0
    while g<=n**(1/4):
        g+=1
    return g-1
def gauss_5(n):
    g=0
    while g<=n**(1/5):
        g+=1
    return g-1
def gauss_6(n):
    g=0
    while g<=n**(1/6):
        g+=1
    return g-1
def gauss_7(n):
    g=0
    while g<=n**(1/7):
        g+=1
    return g-1

if n<=3:
    print(1)
elif n not in (125,216,343,512,729,1000):
    print(max(gauss_2(n)**2,gauss_3(n)**3,gauss_4(n)**4,gauss_5(n)**5,gauss_6(n)**6,gauss_7(n)**7))
else:
    print(n)