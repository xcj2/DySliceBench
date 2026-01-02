from sys import stdin

def Int_all(): return list(map(int, stdin))
def IL():return list(map(int, stdin.readline().split()))


def dfs(i,s):

	if i == 4:
		return s==7

	if dfs(i+1,s+a[i]):
		if i != 0:
			ans[i] = "+"+str(a[i])
		else:
			ans[i] = str(a[i])
		return True
	if dfs(i+1, s-a[i]):
		if i != 0:
			ans[i] = "-"+str(a[i])
		else:
			ans[i] = str(a[i])
		
		return True

	return False



a = list(map(int,list(input())))
ans = [0 for i in range(4)]

def main():
	dfs(0,0)
	print("{}=7".format(''.join(ans)))

if __name__ == "__main__": main()