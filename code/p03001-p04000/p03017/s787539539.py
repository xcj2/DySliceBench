N,A,B,C,D = map(int,input().split())
S = input()
sunuke = A
hunuke = B

def syori1(sunuke,hunuke):
    while hunuke<D:
        if hunuke+1 == N:
            return "Yes"
        if S[hunuke+1] == ".":
            hunuke += 2
        elif S[hunuke] == ".":
            hunuke += 1
        else:
            return "No"
    
    while sunuke<C:
        if sunuke + 1 == N:
            return "Yes"
        if S[sunuke+1] == ".":
            sunuke += 2
        elif S[sunuke] == ".":
            sunuke += 1
        else:
            return "No"
    
    return "Yes"

def canover():
    for i in range(B-2,D-1):
        if S[i] == "." and S[i+1] == "." and S[i+2]==".":
            return True
        else:
            pass
    return False
    
def tonari():
    if S[B]==".":
        return True
    else:
        return False

if C > D:
    if A+1 == B:
        if tonari():
            print(syori1(sunuke,hunuke))
            exit()
            
    if canover():
        print(syori1(sunuke,hunuke))
    else:
        print("No")
else:
    print(syori1(sunuke,hunuke))