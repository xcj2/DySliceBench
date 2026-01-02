#functions for getting rows and columns
def getRow(graph, index):
  return graph[index]
def getElem(row, index):
  return row[index]
def getAbove(graph, h, w):
  try:
    return getElem(getRow(graph, h-1), w)
  except:
    return "#"
def getBelow(graph, h, w):
  try:
    return getElem(getRow(graph, h+1), w)
  except:
    return "#"
def getRight(graph, h, w):
  try:
    return getElem(getRow(graph, h), w+1)
  except:
    return "#"
def getLeft(graph, h, w):
  try:
    return getElem(getRow(graph, h), w-1)
  except:
    return "#"

#getting input
h, w = [int(x) for x in input().split()]
graph = []
for hh in range(h):
  graph.append(input())


#processing
pos = "Yes"
for height in range(h):
  if pos == "No":
    break
  for width in range(w):
    element = getElem(getRow(graph, height), width)
    if element == ".":
      continue
    else:
      if getAbove(graph, height, width) == "#":
        continue
      elif getBelow(graph, height, width) == "#":
        continue
      elif getRight(graph, height, width) == "#":
        continue
      elif getLeft(graph, height, width) == "#":
        continue
      else:
        pos = "No"
        break


print(pos)