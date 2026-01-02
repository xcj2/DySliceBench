class dice:
    def __init__(self,label):
        self.label = {i+1: l for i,l in enumerate(label)}
    def roll(self,op):
        l = self.label
        if   op=='N': self.label = {1:l[2], 2:l[6], 3:l[3], 4:l[4], 5:l[1], 6:l[5]}
        elif op=='E': self.label = {1:l[4], 2:l[2], 3:l[1], 4:l[6], 5:l[5], 6:l[3]}
        elif op=='W': self.label = {1:l[3], 2:l[2], 3:l[6], 4:l[1], 5:l[5], 6:l[4]}
        elif op=='S': self.label = {1:l[5], 2:l[1], 3:l[3], 4:l[4], 5:l[6], 6:l[2]}
    def yaw(self,op):
        l = self.label
        if   op=='CW' : self.label = {1:l[1], 2:l[3], 3:l[5], 4:l[2], 5:l[4], 6:l[6]}
        elif op=='CCW': self.label = {1:l[1], 2:l[4], 3:l[2], 4:l[5], 5:l[3], 6:l[6]}
    def get_label(self,i=0):
        if 1 <= i <= 6:
            return self.label[i]
        else:
            return [self.label[x] for x in range(1,7)] 

def cmp_dice(d0,d1):
    dc = dice(d0.get_label())
    d1_l = d1.get_label()
    result=False
    if set(dc.get_label())==set(d1_l):
        for i in range(6):
            for _ in range(4):
                if dc.get_label()==d1_l:
                    result=True
                    break
                dc.yaw('CW')
            if dc.get_label()==d1_l:
                break
            if i < 4:
                dc.roll('E')
            if i >= 3:
                dc.roll('N')
            if i >= 4:
                dc.roll('N')
    return result

if __name__ == '__main__':
    import itertools
    n=int(input())
    d_list = [dice(list(map(int, input().split()))) for _ in range(n)]
    result='Yes'
    for dx, dy in itertools.combinations(d_list,2):
        if cmp_dice(dx,dy):
            result='No'
            break
    print(result)