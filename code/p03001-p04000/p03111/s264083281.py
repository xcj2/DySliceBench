def abc119_c():
  n, a, b, c = map(int, input().split())
  L = [int(input()) for _ in range(n)]
  ans = 10**9

  def dfs(arr):
    if len(arr) == n:
      # ABCともに材料が1つ以上あるなら得点計算する
      if arr.count(1) > 0 and arr.count(2) > 0 and arr.count(3) > 0:
        calc_score(arr)
      return
    for i in range(4):
      dfs(arr + [i])

  def calc_score(arr):
    nonlocal ans
    # パターンにあわせて棒を用意する
    tools_a = [L[i] for i in range(n) if arr[i] == 1]
    tools_b = [L[i] for i in range(n) if arr[i] == 2]
    tools_c = [L[i] for i in range(n) if arr[i] == 3]
    # 得点計算して答えを更新
    score = magic(tools_a, a)
    score += magic(tools_b, b)
    score += magic(tools_c, c)
    ans = min(score, ans)

  def magic(tools, target):
    # 延長短縮で長さ合わせにいく
    pt = abs(target - sum(tools))
    # 棒が複数あると合成コスト追加、棒の数マイナス1
    if len(tools) >= 2:
      pt += 10 * (len(tools) - 1)
    return pt

  dfs([])
  print(ans)

abc119_c()