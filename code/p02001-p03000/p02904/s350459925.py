class MinSlideWindow:
    def __init__(self,p):
        self.pos_list = []
        self.val_list = p
        self.start_idx = 0

    def put(self,pos):
        val = self.val_list[pos]

        while len(self.pos_list) > self.start_idx:
            pos1 = self.pos_list[-1]
            val1 = self.val_list[pos1]
            if val1 >= val:
                del self.pos_list[-1]
            else:
                break
        self.pos_list.append(pos)

    def get(self,pos):
        while len(self.pos_list) > self.start_idx:
            pos1 = self.pos_list[self.start_idx]
            if pos1 <= pos:
                self.start_idx += 1
            else:
                break

    def min(self):
        pos1 = self.pos_list[self.start_idx]
        val1 = self.val_list[pos1]
        return val1

class MaxSlideWindow:
    def __init__(self,p):
        self.pos_list = []
        self.val_list = p
        self.start_idx = 0
        
    def put(self,pos):
        val = self.val_list[pos]

        while len(self.pos_list) > self.start_idx:
            pos1 = self.pos_list[-1]
            val1 = self.val_list[pos1]
            if val1 <= val:
                del self.pos_list[-1]
            else:
                break
        self.pos_list.append(pos)

    def get(self,pos):
        while len(self.pos_list) > self.start_idx:
            pos1 = self.pos_list[self.start_idx]
            if pos1 <= pos:
                del self.pos_list[self.start_idx]
            else:
                break

    def max(self):
        pos1 = self.pos_list[self.start_idx]
        val1 = self.val_list[pos1]
        return val1




s = input().split(" ")
n = int(s[0])
k = int(s[1])
sp = input().split(" ")
p = [int(pstr) for pstr in sp]
num = 1
ident = True
rv_pos = -1

minw = MinSlideWindow(p)
maxw = MaxSlideWindow(p)

for i in range(k - 1):
    if p[i] > p[i + 1]:
        rv_pos = i
        ident = False
    
for i in range(k-1):
    minw.put(i)
    maxw.put(i)

for i in range(1,n - k + 1):
    
    maxw.put(i + k - 2)
    minw.put(i + k - 2)
    maxw.get(i-1)
    minw.get(i-1)

    """    
    for j in range(k - 1):
        if p[i + j] > p[i + j +1]:
            break
    else:
        if not ident:
            ident = True
            num += 1
        continue
    """
    if p[i + k - 2] > p[i + k - 1]:
        rv_pos = i + k - 2
        

    
    if rv_pos < i:
        if not ident:
            ident = True
            num += 1
        continue
            

    if p[i - 1] > minw.min() or p[i + k - 1] < maxw.max():
        num += 1

    
print(num)
