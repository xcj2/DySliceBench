import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import copy
import queue

def main():
    mod=10**9+7
    N=I()
    q=queue.Queue()
    q.put("a")
    ans=[]
    
    
    while True:
        s=q.get()
        if len(s)==N:
            q.put(s)
            break
        s2=list(copy.deepcopy(s))
        s2.sort()
        big=ord(s2[-1])-97
        for i in range(big+2):
            q.put(s+chr(i+97))
            
    while not q.empty():
        s=q.get()
        ans.append(s)  
    
    ans.sort()
    
    for i in range(len(ans)):
        print(ans[i])

main()

