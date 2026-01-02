# transformation.py
def originalPrint(text,start,end):
    print(text[start: end])
    
def originalReverse(text,start,end):
    head = (text[:start])
    target = (text[start:end])
    sliced = target
    reversed_text = sliced[::-1]
    tail = text[end:]
    # print(head+reversed_text+tail)
    text = head+reversed_text+tail
    return text
    
def orignalReplace(text,start,end, replace_text):
    head = (text[:start])
    tail = text[end:]
    # print(head+replace_text+tail)
    text = head+replace_text+tail
    return text

text = input()
num = int(input())

for i in range(num):
    order_info = input().split()
    order = order_info[0]
    start = int(order_info[1])
    end = int(order_info[2]) + 1
    if order == 'print':
        originalPrint(text, start, end)
    elif order == 'reverse':
        text = originalReverse(text, start, end)
    elif order == 'replace':
        replace_text = order_info[3]
        text = orignalReplace(text, start, end,replace_text)
    
