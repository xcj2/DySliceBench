dai=list(map(int,input().split()))

# dai[0] 上 
# dai[1] 前 
# dai[2] 右
# dai[3] 左
# dai[4] 後
# dai[5] 下

def zenten():
	dai0 = dai[0]
	dai[0] = dai[4]
	dai[4] = dai[5]
	dai[5] = dai[1]
	dai[1] = dai0

def tokei():
	dai1 = dai[1]
	dai[1] = dai[2]
	dai[2] = dai[4]
	dai[4] = dai[3]
	dai[3] = dai1
	
n=int(input())

def check():
	for j in range(4):
		if a == dai[0] and b == dai[1]:
			print(dai[2])
			return True
		tokei()
	return False

for m in range(n):
	a,b=map(int,input().split())
	# a 上の番号
	# b 前の番号
	if not check():# 0
		zenten()
		if not check(): # 4
			zenten()
			if not check(): # 5
				zenten()
				if not check(): # 1
					tokei()
					zenten()
					if not check(): # 3
						zenten()
						zenten()
						if not check(): #2
							print("ERROR")

