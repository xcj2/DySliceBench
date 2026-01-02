def getInt(): return int(input())

class Debug():
    def __init__(self):
        self.debug = True
 
    def off(self):
        self.debug = False
 
    def dmp(self, x, cmt=''):
        if self.debug:
            if cmt != '':
                w = cmt + ': ' + str(x)
            else:
                w = str(x)
            print(w)
        return x

def color(start, tiles):
    count = 0
    for i in range(len(tiles)):
        if i % 2 == 0 and tiles[i] != start:
            count += 1
        elif i % 2 == 1 and tiles[i] == start:
            count += 1
    return count


def prob():
    d = Debug()
    d.off()
    S = input()
    count1 = color('0', S)
    count2 = color('1', S)
    d.dmp((count1,count2),'count1,count2')
    return min(count1, count2)

ans = prob()
print(ans)