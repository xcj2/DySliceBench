class Stack(list):
    def __init__(self):
        self.length = 0
    def __len__(self):
        return self.length

    def push(self,x):
        self.insert(len(self),x)
        self.length += 1
    def pop(self):
        try:
            if(len(self)==0):
                raise NameError("stack is empty")
            tmp = self[len(self)-1]
            self.length -= 1
            return tmp
        except:
            print("stack is empty!!!!")
            return '#'

data = Stack()
s = input()
x = s.split()

for i in x:
    if i == '+':
        a = data.pop()
        b = data.pop()
        data.push(b+a)

    elif i == '-':
        a = data.pop()
        b = data.pop()
        data.push(b-a)


    elif i == '*':
        a = data.pop()
        b = data.pop()
        data.push(b*a)
  
    else:
        data.push(int(i))
print(data.pop())