import math;

def swap(a,b):
    return (b,a)

def gcd(a,b):
    if (a<b):
        a,b = swap(a,b)
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

xm = [1,0,-1,0]
ym = [0,1,0,-1]

def bfs(y,x):
    if (y==gy and x==gx):
        return
    for i in range(4):
        for j in range(4):
            if (c[y+ym[i]][x+xm[j]]=='#'):
                continue
            if (aom[y+ym[i]][x+xm[j]]!=-1):
                continue
            aom[y+ym[i]][x+xm[j]] = aom[y][x] + 1

def main():
    a = int(input())
    s = input()
    if a>=3200:
        print(s)
    else:
        print('red')
    return

if __name__ == '__main__':
    main()