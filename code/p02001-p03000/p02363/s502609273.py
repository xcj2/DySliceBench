def print_solve(ans):
    if "negative" in ans:
        print("NEGATIVE CYCLE")
    else:
        for l in ans:
            for c in l[:-1]:
                if c == float("inf"):
                    print("INF",end=" ")
                else:
                    print(c,end=" ")
            if l[-1] == float("inf"):
                print("INF")
            else:
                print(l[-1])

def solve(graph_data, num_v):
    ans = []

    for i in range(num_v):
        ans.append(partial_solve(graph_data, i, num_v))

    return ans

def partial_solve(graph_data, source, num_v):
    ans = [0 if i == source else float('inf') for i in range(num_v)]

    i = 0
    while (ans != solver_iteration(graph_data, ans)):
        ans = solver_iteration(graph_data, ans)
        i += 1
        if i >= num_v:
            return "negative"

    return ans

def solver_iteration(graph_data, prev_ans):
    new_ans = prev_ans[0:]

    for i, v in enumerate(new_ans):
        if v == float('inf') or i not in graph_data:
            continue

        for t, w in graph_data[i]:
                new_ans[t] = min(new_ans[t], v + w)

    return new_ans

def main():
    l = input().split()
    V = int(l[0])
    E = int(l[1])

    graph = {}
    for i in range(E):
        l = input().split()
        s = int(l[0])
        t = int(l[1])
        d = int(l[2])

        if s in graph:
            graph[s].append((t,d))
        else:
            graph[s] = [(t,d)]

    print_solve(solve(graph, V))

if __name__ == "__main__":
    main()