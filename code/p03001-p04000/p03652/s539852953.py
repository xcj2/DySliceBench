# encoding:utf-8

def main():
	N, M = list(map(int, input().split()))
	prefs = [list(map(int, input().split())) for _ in range(N)]

	game_list = [i for i in range(1, M + 1)]

	tmp = 10 ** 10
	for i in range(M):
		max_game, idx = maxGame(prefs, game_list, M)
		tmp = min(tmp, max_game)
		prefs = removeGame(prefs, idx + 1)
	print(tmp)

def removeGame(prefs, idx):
	for i in range(len(prefs)):
		prefs[i].remove(idx)
	return(prefs)

def maxGame(prefs, game_list, M):
	counter = [0 for _ in range(M)]
	for i in range(len(prefs)):
		counter[prefs[i][0] - 1] += 1
	return([max(counter), counter.index(max(counter))])

if __name__ == '__main__':
	main()