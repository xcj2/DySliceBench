from collections import deque

S = input()
Q = int(input())
Queries = [input().split() for i in range(Q)]

state = {
    "S": S,
    "is_reversed": False,
    "left": deque(),
    "right": deque(),
}

def T1(state):
    state['is_reversed'] = not state['is_reversed']

def T2(state, F, C):
    if not state['is_reversed']:
        if F == '1':
            state['left'].appendleft(C)
        else:
            state['right'].append(C)
    else:
        if F == '1':
            state['right'].append(C)
        else:
            state['left'].appendleft(C)

def output(state):
    output = ''.join(state['left']) + state['S'] + ''.join(state['right'])
    if state['is_reversed']:
        output = ''.join(list(reversed(output)))

    return output


for Query in Queries:
    if Query[0] == '1':
        T1(state)
    else:
        T2(state, Query[1], Query[2])

answer = output(state)

print(answer)
