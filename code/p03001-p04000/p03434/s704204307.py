# _*_ coding:utf-8 _*_
#  Atcoder_Beginners_Contest088-B
#  TODO https://atcoder.jp/contests/abc088/tasks/abc088_b
def calcAlice(cardList):
	cardMany = len(cardList)
	alicePoint = 0
	checkRange = range(0,cardMany,+2)
	for i in checkRange:
		alicePoint = alicePoint + cardList[i]
	return alicePoint

def calcBob(cardList):
	cardMany = len(cardList)
	bobPoint = 0
	checkRange = range(1,cardMany,+2)
	for i in checkRange:
		bobPoint = bobPoint + cardList[i]
	return bobPoint

def  diffTwoScore(allCards,cardsNumberGivenList):
	cardNumberSortedList=sorted(cardsNumberGivenList,reverse=True)
	getScoreForAlice = calcAlice(cardNumberSortedList)
	getScoreForBob = calcBob(cardNumberSortedList)
	diffPoint = getScoreForAlice - getScoreForBob
	answer = diffPoint
	return answer


if __name__ == '__main__':
	N = int(input().strip())
	cardsNumberRawList = list(map(int,input().strip().split(' ')))
	solution=diffTwoScore(N,cardsNumberRawList)
	print("{}".format(solution))