#  --*-coding:utf-8-*--

def f(str):
    numOfX = 0
    numOfXs = []
    letters = []
    
    for c in str:
        if c == 'x':
            numOfX += 1
        else:
            letters.append(c)
            numOfXs.append(numOfX)
            numOfX = 0
            
    numOfXs.append(numOfX)

    for i in range(len(letters)//2):
        if letters[i] != letters[-i-1]:
            return -1

    a = 0
    for i in range(len(numOfXs)//2):
        a += abs(numOfXs[i] - numOfXs[-i-1])
            
    return a

def test():
    assert f('xabxa') == 2
    assert f('ab') == -1
    assert f('a') == 0
    assert f('oxxx') == 3


def main():
    str = input()
    print(f(str))

if __name__ == '__main__':
    main()

