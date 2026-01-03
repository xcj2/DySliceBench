import math

def cceil(x,y):
	res = x //y
	if x % y != 0:res += 1
	return res

def gcd(x, y):
	if(x == 0):return y
	return gcd(y % x, x)
 
def main():
    votes = int(input())
    ratio = [[ int(i) for i in input().split() ] for j in range(votes)]
 
    votesTemp = [0, 0]
    for i in range(votes):
        if i == 0:
            votesTemp = ratio[i]
            continue
        if(gcd(ratio[i][0], ratio[i][1]) != 1):
        	x = 1 / 0
        ceil = [ cceil(votesTemp[j], ratio[i][j]) for j in range(2)]
 
        votesTemp = [ max(ceil) * ratio[i][j] for j in range(2) ]
        
        #print("turn: " + str(i))
        #print("votes: " + str(ratio[i][0]) + ":" + str(ratio[i][1]) )
        #print("Temp: " +str(votesTemp[0])+":"+str(votesTemp[1]))
        
    print(sum(votesTemp))
 
if __name__ == '__main__':
  main()
