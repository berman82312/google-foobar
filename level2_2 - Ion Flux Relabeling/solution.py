def find_top(h):
  top = 2**h - 1
  def find_top_of(x):
    if x == top:
      return -1
    current_top = top
    level = h
    while level > 0:
      left = current_top - 2**(level-1)
      if x == left:
        return current_top
      elif x == (current_top - 1):
        return current_top
      elif x < left:
        current_top = left
      else:
        current_top = current_top - 1
      level -= 1
    return -1
  return find_top_of

def solution(h, q):
  result = map(find_top(h), q)
  return result
