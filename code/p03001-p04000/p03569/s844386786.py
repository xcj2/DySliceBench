#  --*-coding:utf-8-*--

# CODE FESTIVAL 2017 qual C
# C - Inserting 'x'
# http://code-festival-2017-qualc.contest.atcoder.jp/tasks/code_festival_2017_qualc_c

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

    if any(letters[i] != letters[-i-1] 
           for i in range(len(letters)//2)):
        return -1

    return sum(abs(numOfXs[i] - numOfXs[-i-1]) 
            for i in range(len(numOfXs)//2))

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

