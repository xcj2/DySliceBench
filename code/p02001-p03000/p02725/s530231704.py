def bubbleSort(array):
    sortCompleted = False
    while sortCompleted != True:
        sortCompleted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sortCompleted = False

def getMaxDistance(array):
    maxDistance = 0
    for i in range(len(array)-1):
        distance = abs(array[i] - array[i+1])
        if maxDistance < distance:
            maxDistance = distance
    return maxDistance

def function(K, An): 
    bubbleSort(An)
    An.append(K+An[0])
    maxDistance = getMaxDistance(An)
    minDistance = K - maxDistance
    return str(minDistance)

if __name__ == '__main__':
    K, N = map(int, input().split())
    An = list(map(int,input().split()))
    print(function(K, An))
