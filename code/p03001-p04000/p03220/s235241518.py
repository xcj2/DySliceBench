import sys
 
def solve(N, T, A, ls_H):
    temperature = []
    difference = []
    near = []
    ti = 10**5//1
    for x in ls_H :
        air = T - x * 0.006
        temperature.append(air)
    #print(temperature)
    
    for y in temperature :
        til = A - y
        difference.append(til)
    #print(difference)
    
    for z in difference :
        near.append(abs(z))
    #print(near)
    
    for i in near :
        if ti > i :
            ti = i
    #print(ti)
    return near.index(ti) + 1


def readQuestion():
    ws = sys.stdin.readline().strip().split()
    N = int(ws[0])
    ws = sys.stdin.readline().strip().split()
    T = int(ws[0])
    A = int(ws[1])
    ws = sys.stdin.readline().strip().split()
    ls_H = list(map(int, ws))
    return (N, T, A, ls_H)
 
def main():
    print(solve(*readQuestion()))
 # Uncomment before submission
main()