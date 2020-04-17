def bfs(start, maze):
  y_len = len(maze)
  x_len = len(maze[0])
  result = [[None for _ in xrange(x_len)] for _ in xrange(y_len)]
  result[start[1]][start[0]] = 1
  next_points = [start]
  for current in next_points:
    x, y = current
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for move in movements:
      x2 = x + move[0]
      y2 = y + move[1]
      if 0 <= x2 < x_len and 0 <= y2 < y_len:
        if result[y2][x2] is None:
          result[y2][x2] = result[y][x] + 1
          if maze[y2][x2] == 0:
            next_points.append((x2, y2))
  return result

def solution(maze):
  y_len = len(maze)
  x_len = len(maze[0])
  pe = bfs((0,0), maze)
  ep = bfs((x_len - 1, y_len - 1), maze)
  steps = x_len * y_len
  for x in xrange(x_len):
    for y in xrange(y_len):
      if ep[y][x] and pe[y][x]:
        step = pe[y][x] + ep[y][x] - 1
        steps = min(step, steps)
  return steps
