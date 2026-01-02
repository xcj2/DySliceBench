from sys import setrecursionlimit

setrecursionlimit(3 * 10 ** 5)

def main():
  n, m, k = map(int, input().split(' '))
  nodes = tuple([([], set()) for i in range(n)])
  for _ in range(m):
    a, b = sorted(map(lambda x: int(x) - 1, input().split()))
    nodes[a][0].append(b)
    nodes[b][0].append(a)

  for _ in range(k):
    c, d = sorted(map(lambda x: int(x) - 1, input().split()))
    nodes[c][1].add(d)
    nodes[d][1].add(c)

  total_done_set = set()

  def dfs(node_id, done_set):
    if node_id in done_set: return 0

    total_done_set.add(node_id)
    done_set.add(node_id)

    size = 1
    for child_id in nodes[node_id][0]:
      size += dfs(child_id, done_set)

    return size


  ans_list = [-1] * n

  def dfs2(node_id, connected_ids, total_len):
    children, block_id_set = nodes[node_id]
    ans_list[node_id] = total_len - len(list(filter(
      lambda block_id: block_id in connected_ids, block_id_set
    ))) - 1

    except_num = 0
    for child_id in children:
      if child_id not in block_id_set:
        except_num += 1

      if ans_list[child_id] == -1:
        dfs2(child_id, connected_ids, total_len)

    ans_list[node_id] -= except_num


  for i in range(n):
    if i not in total_done_set:
      done_set = set()
      dfs(i, done_set)
      dfs2(i, done_set, len(done_set))

  print(*ans_list, sep=" ")


main()
