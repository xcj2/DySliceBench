import math

def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

def printParent(i,h):
    parent=math.floor(i/2)
    if(parent>0):
        print('parent key = {}, '.format(h[parent]),end='')

def printLeft(i,h):
    left=2*i
    if(left<=len(h[1:])):
        print('left key = {}, '.format(h[left]),end='')

def printRight(i,h):
    right=2*i+1
    if(right<=len(h[1:])):
        print('right key = {}, '.format(h[right]),end='')

def main(n,h):
    h.insert(0,-1)
    for i in range(1,n+1):
        print('node {}: key = {}, '.format(i, h[i]),end='')
        printParent(i,h)
        printLeft(i,h)
        printRight(i,h)
        print('')

    return

if __name__=='__main__':
    n,h=readinput()
    main(n,h)
