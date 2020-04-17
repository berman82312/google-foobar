def carry_in_remain(distance, remains, start, end, time_left):
  if len(remains) == 0:
    time_spent = distance[start][end]
    if time_spent <= time_left:
      return [start]
    else:
      return False
  else:
    time_spent = distance[start][end]
    max_carried = []
    can_reach = False
    if time_spent <= time_left:
      # if directly go to exit
      max_carried.append(start)
      can_reach = True
    for m in remains:
      time_spent = distance[start][m]
      current_left = remains[:]
      current_left.remove(m)
      carry = carry_in_remain(distance, current_left, m, end, time_left - time_spent)
      if carry:
        carry.append(start)
        if len(carry) > len(max_carried):
          max_carried = carry
          can_reach = True
    if can_reach:
      return max_carried
    else:
      return False

def solution(times, times_limit):
  distance = []
  # Bellman-Ford for every i->j
  for m in xrange(len(times)):
    shortest = times[m]
    for _ in xrange(len(times)):
      for i in xrange(len(times)):
        for j in xrange(len(times)):
          if i == j:
            continue
          temp = shortest[i] + times[i][j]
          if temp < shortest[j]:
            shortest[j] = temp
    distance.append(shortest)
  # do one more to check negative circle
  for i in xrange(len(times)):
    for j in xrange(len(times)):
      if i == j:
        continue
      temp = distance[0][i] + times[i][j]
      if temp < distance[0][j]:
        # print(range(len(times) - 2))
        return range(len(times) - 2)
  remains = list(range(1, len(times) - 1))
  max_carried = []
  start = 0
  end = len(times) - 1
  # find the longest path we can travel
  for m in remains:
    time_spent = distance[start][m]
    current_left = remains[:]
    current_left.remove(m)
    carry = carry_in_remain(distance, current_left, m, end, times_limit - time_spent)
    if carry:
      if len(carry) > len(max_carried):
        max_carried = carry[:]
  max_carried.sort()
  result = [x - 1 for x in max_carried]
  # print(result)
  return result
