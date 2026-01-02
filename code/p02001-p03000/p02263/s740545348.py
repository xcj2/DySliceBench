# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=jp
class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)
    
    def pop(self):
        item = self.elements[-1]
        del self.elements[-1]
        return item

def putsarray(array):
    if len(array) == 0:
        return
    for i in range(len(array) - 1):
        print(array[i], end=' ')
    print(array[-1])

def get_operands(st):
    # オペランドの順番は逆に格納されている
    op2 = st.pop()
    op1 = st.pop()
    return op1, op2

if __name__ == "__main__":
    st = Stack()
    array = input().split()
    for symbol in array:
        if symbol == "*":
            op1, op2 = get_operands(st)
            st.push(op1 * op2)
        elif symbol == "+":
            op1, op2 = get_operands(st)
            st.push(op1 + op2)
        elif symbol == "-":
            op1, op2 = get_operands(st)
            st.push(op1 - op2)
        else:
            st.push(int(symbol))
    print(st.pop())
