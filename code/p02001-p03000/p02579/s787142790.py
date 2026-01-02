import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def toi(h,w):
	return h*10000 + w
	
def fromi(v):
	return v//10000, v%10000

def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	ch, cw = tin()
	start_h,start_w = ch-1,cw-1
	dh,dw = tin()
	goal_h, goal_w=dh-1, dw-1
	ll=[input() for _ in range(h)]
	pll=[[-1]*w for _ in range(h)]
	egg = [[] for _ in range(w*h)]
	
	mark=-1
	for hi in range(h):
		for wi in range(w):
			if ll[hi][wi]=='#':
				continue
			if pll[hi][wi] >= 0:
				continue
			mark+=1
			qq=collections.deque()
			qq.append(toi(hi,wi))
			open_list=set()
			open_list.add(toi(hi,wi))
			while len(qq)>0:
				nv = qq.popleft()
				nh, nw = fromi(nv)
				pll[nh][nw] = mark
				for dh,dw in [[1,0], [-1,0], [0,1], [0,-1]]:
					if nh + dh < 0 or nh + dh >= h:
						continue
					if nw + dw < 0 or nw + dw >= w:
						continue
					if toi(nh+dh,nw+dw) in open_list:
						continue
					if ll[nh + dh][nw+dw]=='#':
						egg[mark].append([nh,nw,dh,dw])
						continue
					if pll[nh + dh][nw+dw] > 0:
						continue
					qq.append(toi(nh + dh, nw+dw))
					open_list.add(toi(nh+dh,nw+dw))
					
	#print(pll)
	if pll[start_h][start_w] == pll[goal_h][goal_w]:
		return 0
	#for l in egg:	
	#	print(l)
	
	qqq=collections.deque()
	qqq.append((pll[start_h][start_w],0))
	g_pos=pll[goal_h][goal_w]
	open_list=set()
	open_list.add(-1)
	#pa('tttt')
	while len(qqq)>0:
		pos, cost = qqq.popleft()
		if pos == g_pos:
			return cost
		for [nh,nw,_h,_w] in egg[pos]:
			for dh in [-2,-1,0,1,2]:
				for dw in [-2,-1,0,1,2]:
					nnh = nh + dh
					nnw = nw + dw
					if nnh < 0 or nnh >= h:
						continue
					if nnw < 0 or nnw >= w:
						continue
					vv = pll[nnh][nnw]
					if vv in open_list:
						continue
					qqq.append((vv, cost+1))
					open_list.add(vv)
					#pa((vv,g_pos))
		
	return -1
		
		
			
		
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)