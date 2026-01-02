def cross(v1,v2):
	return v1.real*v2.imag-v1.imag*v2.real

def isOnSegment(p1,p2,p):
	return abs(p1-p)+abs(p2-p)-abs(p1-p2)<=1e-8

def isIntersection(p1,p2,p3,p4):
	if cross(p2-p1,p4-p3)==0:
		return any(isOnSegment(q1,q2,q3)for q1,q2,q3 in ((p1,p2,p3),(p1,p2,p4),(p3,p4,p1),(p3,p4,p2)))
	return cross(p2-p1,p3-p1)*cross(p2-p1,p4-p1)<=1e-8>=cross(p4-p3,p1-p3)*cross(p4-p3,p2-p3)

import sys
input = sys.stdin.buffer.readline
ans=[]
for _ in range(int(input())):
	m=map(int,input().split())
	ans.append(int(isIntersection(*[complex(x,y)for x,y in zip(*[iter(m)]*2)])))
print("\n".join(map(str,ans)))
