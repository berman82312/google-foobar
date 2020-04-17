def get_paths(tree, exits):
  paths = []
  for i in exits:
    if tree[i]['previous'] == 0:
      paths.append([i])
    else:
      previous_paths = get_paths(tree, tree[i]['previous'])
      for p in previous_paths:
        p.append(i)
        paths.append(p)
  return paths

def solution(entrances, exits, path):
  room_amount = len(path)
  start_amount = [0 for _ in path]
  flow = 0
  #step 1: merge entrances
  for i in entrances:
    for j in xrange(room_amount):
      if j in entrances:
        continue
      elif j in exits:
        flow += path[i][j]
      else:
        start_amount[j] += path[i][j]
  # Dinic's algorithm
  more_flow = True
  while more_flow:
    ## BFS
    more_flow = False
    room_tree = [{'previous': 0  ,'level': 1, 'next': []} if start_amount[i] > 0 else {'previous': [], 'level': None, 'next': []} for i in xrange(room_amount)]
    room_level = [None for _ in path]
    bfs = []
    for i in xrange(room_amount):
      if start_amount[i] > 0:
        bfs.append(i)
        room_level[i] = 1
    for i in bfs:
      if i in exits:
        more_flow = True
        continue
      for j in xrange(room_amount):
        if i == j:
          continue
        if j in entrances:
          continue
        if path[i][j] > 0:
          if room_tree[j]['level'] is None:
            room_tree[j]['level'] = room_tree[i]['level'] + 1
            bfs.append(j)
          if (room_tree[i]['level'] + 1) == room_tree[j]['level']:
            room_tree[i]['next'].append(j)
            room_tree[j]['previous'].append(i)
        else:
          continue
    paths = get_paths(room_tree, exits)
    ## DFS
    for p in paths:
      max_flow = 0
      for i in xrange(len(p)):
        if i == 0:
          max_flow = start_amount[p[i]]
        else:
          temp_flow = path[p[i-1]][p[i]]
          max_flow = min(max_flow, temp_flow)
      if max_flow > 0:
        flow += max_flow
      for i in xrange(len(p)):
        if i == 0:
          start_amount[p[i]] -= max_flow
        else:
          path[p[i-1]][p[i]] -= max_flow
          path[p[i]][p[i-1]] += max_flow
  # print(flow)
  return flow
