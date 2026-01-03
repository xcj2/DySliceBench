from heapq import heapify, heappop, heappush
N=int(input())
A=list(map(int, input().split()))

class MaxHeap:
    def __init__(self, li):
        self.hp = []
        for e in li:
            heappush(self.hp, -e)

    def push(self, x):
        heappush(self.hp, -x)

    def pop(self):
        ret = heappop(self.hp)
        ret *= -1
        return ret

    def seak(self):
        return -self.hp[0]

    def sum(self):
        return -sum(self.hp)

A1=A[:N]
A2=A[N:2*N]
A3=A[2*N:]

heapify(A1)
A1_sum=sum(A1)
A1_li=[A1_sum]
for a in A2:
  heappush(A1, a)
  p=heappop(A1)
  A1_sum+=a-p
  A1_li.append(A1_sum)
  
A3_sum=sum(A3)
A3=MaxHeap(A3)

A3_li=[A3_sum]
for a in A2[::-1]:
  A3.push(a)
  A3_sum+=a
  p=A3.pop()
  A3_sum-=p
  A3_li.append(A3_sum)
  
A3_li=A3_li[::-1]  
ans=False
for a1, a3 in zip(A1_li, A3_li):
  if not ans:
    ans=a1-a3
  else:
    ans=max(ans, a1-a3)
print(ans)