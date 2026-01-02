
s = input()

firstTile = s[0]
lastTile = s[-1]

def isOneColor():
    t = None
    for c in s:
        if t is None:
            t = c
        else:
            if c is not t:
                return False
    return True

def reverse(tile):
    if tile is "0":
        return "1"
    else:
        return "0"

def shouldZeroStart():
    z = 0
    o = 0
    currentTile = "0"
    for tile in s:
        if tile is not currentTile:
            z = z + 1
        currentTile = reverse(currentTile)
    currentTile = "1"
    for tile in s:
        if tile is not currentTile:
            o = o + 1
        currentTile = reverse(currentTile)
    if z < o:
        return True
    else:
        return False

result = 0
currentTile = "1"
if isOneColor():
    if firstTile is "0":
        currentTile = "0"
else:
    if shouldZeroStart():
        currentTile = "0"
for i in range(len(s)):
    if s[i] is not currentTile:
        result = result + 1
    currentTile = reverse(currentTile)



print(result)
