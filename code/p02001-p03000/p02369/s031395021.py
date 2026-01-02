# トポロジカルソート
def main():
    Graph = [] ##appendのために宣言が必要
    V,E = map(int,input().split())
    # V：頂点数
    # E：辺数
    # 入力受付
    i = 0
    while i < E:
        try:
            Graph.append(list(map(int,input().split())))
            i = i + 1
        except:
            break;
            #または、quit(),os.exit()をして止める。

    point_dict = {}
    result = topological_sort(V,E,Graph,point_dict)
    print(result)

# 初期化
def initialize(v,pdict):
    i = 0
    while i < v:
        pdict[i] = 0
        i = i + 1
    return pdict

# 辺の数計算
def count_node(graph,pdict):
    i = 0
    while i < len(graph):
        pdict[graph[i][1]] = pdict[graph[i][1]] + 1
        i = i + 1
    return pdict

# 入り辺がない点を除去
def remove_point(graph,pdict):
    i = 0
    count_remove = 0
    # 入り辺がない点を探索
    while i < len(pdict):
        if pdict[i] == 0:
            m = 0
            while m < len(graph):
                # 入り辺がない頂点が始点になっている行を削除
                # i : 入り辺がない点の番号
                if graph[m][0] == i:
                    graph.pop(m)
                    # popすると行列のサイズが一つ減るので
                    m = m - 1
                    count_remove = count_remove + 1
                m = m + 1
        i = i + 1
    return (graph,count_remove)

def topological_sort(v,e,graph,pdict):
    pdict = initialize(v, pdict)
    pdict = count_node(graph,pdict)
    """
    print()
    print("Graph")
    print(graph)
    print("pdict")
    print(pdict)
    """
    graph,count_remove = remove_point(graph, pdict)
    """
    print("Graph_Remove")
    print(graph)
    print(count_remove)
    print("-----------------------------")
    """
    if len(graph) == 0:
        return 0
    elif count_remove == 0:
        return 1
    elif count_remove > 0:
        return topological_sort(v,e,graph,pdict)


if __name__ == '__main__':
    main()

