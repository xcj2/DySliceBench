class Bubblesort():
    def __init__(self,x,n):
        self.C = x
        self.n = n
    def sorting(self):
        for i in range(self.n):
            for j in range(self.n - 1 , i , -1):
                if int(self.C[j][1]) < int(self.C[j - 1][1]):
                    self.C[j], self.C[j - 1] = self.C[j - 1], self.C[j]
        return self.C
    
    def check(self, xx):
        return CheckStable(self.C, xx)

class Selectionsort():
    def __init__(self, x, n):
        self.C = x
        self.n = n
    def sorting(self):
        for i in range(0, self.n):
            minj = i
            for j in range(i+1, self.n):
                if int(self.C[j][1])  < int(self.C[minj][1]):
                    minj = j
            self.C[i], self.C[minj] = self.C[minj], self.C[i]
        return self.C
    
    def check(self, xx):
        return CheckStable(self.C, xx)
    
def CheckStable(x1, xx2):
    ch1 = []
    for i in range(n - 1):
        if x1[i][1] == x1[i + 1][1]:
            ch1.append(x1[i])
            if i + 1 == n - 1:
                ch1.append(x1[i + 1])
        elif x1[i - 1][1] == x1[i][1]:
            ch1.append(x1[i])
    
    ch2 = []
    x2 = xx2
    for i in ch1:
        for j in range(len(x2)):
            if i[1] == x2[j][1]:
                ch2.append(x2[j])
                x2.pop(j)
                break

    if ch1 == ch2:
        return ('Stable')
    else:
        return ('Not stable')

n = int(input())
x = input().split()
xx =x[:]
y =x[:]
yy =x[:]

a = Bubblesort(x, n)
b = Selectionsort(y, n)
print(' '.join(a.sorting()))
print(a.check(xx))
print(' '.join(b.sorting()))
print(b.check(yy))
