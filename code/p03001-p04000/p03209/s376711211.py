def getItems(layerCount):
	if layerCount == 0:
		return 1
	return 2*getItems(layerCount-1) + 3

def getPats(layerCount):
	return 2**(layerCount + 1) - 1

def patEaten(layer, toEat):
	pattyCount = 0

	if layer == 1:
		burger = "BPPPB"

		for x in range(toEat):
			if burger[x] == "P":
				pattyCount += 1
		return pattyCount
		
	elif layer == 0:
		if toEat == 1:
			return 1
		else:
			return 0
	
	else:
		items = getItems(layer)
		if toEat == items:
			pattyCount += getPats(layer)
			return pattyCount
		elif toEat < 2+getItems(layer-1):
			if items + 1 == 2* toEat:
				toEat-=2
				return 1 + patEaten(layer - 1, toEat)
			toEat -= 1
			return patEaten(layer - 1, toEat)
		else:
			toEat -= (1+1+getItems(layer-1))
			pattyCount += 1 + getPats(layer-1)
			
			return pattyCount + patEaten(layer-1, toEat)

i, j = [int(x) for x in input().split()]
#print(patEaten(2,13))
print(patEaten(i,j))