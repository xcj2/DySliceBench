import sys
readline = sys.stdin.readline


def main():
    a,b,q = map(int,readline().split())
    A = [int(readline()) for i in range(a)]
    B = [int(readline()) for i in range(b)]
    def search(A,x):
        left =0
        right = len(A)-1
        
        if x<A[0]:
            return (float('inf'),abs(x - A[left]))
        if x >A[-1]:
            return (abs(x - A[right]),float('inf'))
        
        while left != right-1:
            center = (left+right)//2
            
            if A[center] > x:
                right = center
            else:
                left = center
        
        return (abs(x - A[left]),abs(x - A[right]))
    
    
    def dist(A,x,lr):
        if lr == float('inf'):
            return float('inf')
        return abs(x - A[lr])
    
    for _ in range(q):
        x = int(readline())
        sl,sr = search(A,x)
        tl,tr = search(B,x)
        print(min(min(sl,sr)+min(tl,tr)+min(min(sl,sr),min(tl,tr)),max(sl,tl),max(sr,tr)))

if __name__ == '__main__':
    main()