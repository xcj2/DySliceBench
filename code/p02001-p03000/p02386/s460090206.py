class Dice:
    def __init__(self,u,s,e,w,n,d):
        self.u = u
        self.s = s
        self.e = e
        self.w = w
        self.n = n
        self.d = d
    
    def rot(self,way):
        # vertically
        if way == 0:
            c = self.u
            self.u = self.n
            self.n = self.d
            self.d = self.s
            self.s = c
        #rotate
        if way == 1:
            c = self.e
            self.e = self.n
            self.n = self.w
            self.w = self.s
            self.s = c
        #holizantally
        if way == 2:
            c = self.w
            self.w = self.d
            self.d = self.e
            self.e = self.u
            self.u = c

def compare(inp1,inp2):
    if not inp1[0] in inp2:
        return 'No'
    dice1 = Dice(inp1[0],inp1[1],inp1[2],inp1[3],inp1[4],inp1[5])
    dice2 = Dice(inp2[0],inp2[1],inp2[2],inp2[3],inp2[4],inp2[5])
    count = 0
    flag = 0
    while True:
        if dice1.u == dice2.u:
            for s in range(5):
                if dice1.s == dice2.s and dice1.e == dice2.e and dice1.w == dice2.w and dice1.n == dice2.n:
                    if dice1.d == dice2.d:
                        flag = 1
                        return 'Yes'
                    break
                else:
                    dice2.rot(1)
            if not flag:
                if dice1.d == dice2.s and dice1.u == dice2.n:
                    if (dice1.s == dice2.u) and (dice1.n == dice2.d) and (dice1.e == dice2.e) and (dice1.w == dice2.w):
                        return 'Yes'
                    else:
                        return 'No'
                elif dice1.d == dice2.e and dice1.u == dice2.w:
                    if (dice1.s == dice2.s) and (dice1.n == dice2.n) and (dice1.e == dice2.u) and (dice1.w == dice2.d):
                        return 'Yes'
                    else:
                        return 'No'
                elif dice1.d == dice2.w and dice1.u == dice2.e:
                    if (dice1.s == dice2.s) and (dice1.n == dice2.n) and (dice1.e == dice2.d) and (dice1.w == dice2.u):
                        return 'Yes'
                    else:
                        return 'No'
                elif dice1.d == dice2.n and dice1.u == dice2.s:
                    if (dice1.s == dice2.d) and (dice1.n == dice2.u) and (dice1.e == dice2.e) and (dice1.w == dice2.w):
                        return 'Yes'
                    else:
                        return 'No'
                else:
                    return 'No'
            break
        elif count < 5:
            dice2.rot(0)
            count += 1
        else:
            dice2.rot(1)
            count = 0
            
times = int(input())
input_list = list()
results = list()
for t in range(times):
    inp = list(map(int,input().split()))
    input_list.append(inp)

for il in input_list:
    for l in input_list:
        if input_list.index(il) != input_list.index(l):
            results.append(compare(il,l))

if 'Yes' in results:
    print('No')
else:
    print('Yes')
