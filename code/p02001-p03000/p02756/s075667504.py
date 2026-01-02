from collections import deque

S = input()
Q = int(input())
Queries = [input().split() for i in range(Q)]

def start(S):
    state = {
        "S": S,
        "is_reversed": False,
        "left": deque(),
        "right": deque(),
    }

    return state


def T1(state, Query):
    state['is_reversed'] = not state['is_reversed']


def T2(state, Query):
    F = Query[1]
    C = Query[2]

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

def fetch(Query):
    operations = {
        '1': T1,
        '2': T2,
    }

    index = Query[0]
    operation = operations[index]

    return operation

def operate(state, Query):
    T = fetch(Query)
    T(state, Query)


def execute(state, Queries):
    state = start(S)

    for Query in Queries:
        operate(state, Query)

    result = output(state)

    return result


answer = execute(S, Queries)

print(answer)
