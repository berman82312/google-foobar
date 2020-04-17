bfs = {'0,0': {'default': 1, 'remodel': None}}
origin_map = None
x_length = 0
y_length = 0

def get_bfs(point):
  global bfs
  x, y = point
  point_key = '{},{}'.format(x, y)
  if point_key not in bfs:
    bfs[point_key] = {
      'default': None,
      'remodel': None
    }
  return bfs[point_key]


def remodel_reach_default(start, end):
  global bfs
  start_bfs = get_bfs(start)
  end_bfs = get_bfs(end)
  end_key = '{},{}'.format(end[0], end[1])
  if end_bfs['remodel'] is None:
    end_bfs['remodel'] = start_bfs['remodel'] + 1
    bfs[end_key] = end_bfs
    return True
  elif end_bfs['remodel'] > (start_bfs['remodel'] + 1):
    end_bfs['remodel'] = (start_bfs['remodel'] + 1)
    bfs[end_key] = end_bfs
    return True
  else:
    return False


def default_reach_remodel(start, end):
  global bfs
  start_bfs = get_bfs(start)
  end_bfs = get_bfs(end)
  end_key = '{},{}'.format(end[0], end[1])
  if start_bfs['default'] is None:
    return False
  if end_bfs['remodel'] is None:
    end_bfs['remodel'] = start_bfs['default'] + 1
    bfs[end_key] = end_bfs
    return True
  elif end_bfs['remodel'] > (start_bfs['default'] + 1):
    end_bfs['remodel'] = start_bfs['default'] + 1
    bfs[end_key] = end_bfs
    return True
  else:
    return False


def default_reach(start, end):
  global bfs
  start_bfs = get_bfs(start)
  end_bfs = get_bfs(end)
  end_key = '{},{}'.format(end[0], end[1])
  modified = False
  if start_bfs['default'] is not None:
    if end_bfs['default'] is None:
      end_bfs['default'] = start_bfs['default'] + 1
      modified = True
    elif end_bfs['default'] > (start_bfs['default'] + 1):
      end_bfs['default'] = start_bfs['default'] + 1
      modified = True
  if start_bfs['remodel'] is not None:
    if end_bfs['remodel'] is None:
      end_bfs['remodel'] = start_bfs['remodel'] + 1
      modified = True
    elif end_bfs['remodel'] > (start_bfs['remodel'] + 1):
      end_bfs['remodel'] = start_bfs['remodel'] + 1
      modified = True
  if modified:
    bfs[end_key] = end_bfs
  return modified


def update(start, end):
  global origin_map
  x1, y1 = start
  x2, y2 = end
  if x2 >= x_length or x2 < 0 or y2 >= y_length or y2 < 0:
    return False
  elif origin_map[y1][x1] == 1 and origin_map[y2][x2] == 1:
    return False
  if origin_map[y1][x1] == 1:
    return remodel_reach_default(start, end)
  elif origin_map[y2][x2] == 1:
    return default_reach_remodel(start, end)
  else:
    return default_reach(start, end)


def solution(the_map):
  global origin_map, y_length, x_length
  y_length = len(the_map)
  x_length = len(the_map[0])
  origin_map = the_map
  next_points = [(0,0)]
  for (x, y) in next_points:
    if update((x, y), (x - 1, y)):
      next_points.append((x - 1, y))
    if update((x, y), (x + 1, y)):
      next_points.append((x + 1, y))
    if update((x, y), (x, y - 1)):
      next_points.append((x, y - 1))
    if update((x, y), (x, y + 1)):
      next_points.append((x, y + 1))
  exit_key = '{},{}'.format(x_length - 1, y_length - 1)
  if bfs[exit_key]['default'] is None:
    return bfs[exit_key]['remodel']
  elif bfs[exit_key]['remodel'] is None:
    return bfs[exit_key]['default']
  else:
    return min(bfs[exit_key]['default'], bfs[exit_key]['remodel'])

# test = [
#       [0,0,0,0,0,0,0,0,0,0],
#       [0,1,1,1,1,1,1,1,1,0],
#       [0,1,0,0,1,1,1,1,1,1],
#       [0,1,0,0,0,0,0,1,1,1],
#       [0,1,1,0,1,1,0,0,0,0],
#       [0,1,1,0,1,1,1,1,1,0],
#       [0,1,1,0,1,1,1,1,1,0],
#       [0,0,0,0,0,1,1,0,0,0],
#       [0,0,0,0,0,0,0,0,0,0],
#       [0,1,1,1,1,1,1,1,1,0],
#       [0,1,1,1,1,1,1,1,1,1],
#       [0,1,1,0,0,0,0,1,1,1],
#       [0,1,1,0,1,1,0,0,0,0],
#       [0,1,1,0,1,1,1,1,1,0],
#       [0,1,1,0,1,1,1,1,1,0],
#       [0,0,0,0,0,1,1,0,0,0]]
# print(solution(test))
