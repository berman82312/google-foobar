def get_cell(n, head, tail):
  a = head
  b = head << 1
  c = tail
  d = tail << 1
  mask = (1 << n) - 1
  result = (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)
  return mask & (result >> 1)

def find_possible_tails(n, row, head, dp):
  if row in dp and head in dp[row]:
    return dp[row][head]
  elif row not in dp:
    dp[row] = {}
  dp[row][head] = []
  for i in xrange(1 << (n + 1)):
    # cellular automation
    result = get_cell(n, head, i)
    if result == row:
      dp[row][head].append(i)
  return dp[row][head]

def is_possible_head(n, row, head):
  # Wipe out T <- TT
  mask = (1 << (n + 1)) - 1
  result = (mask & (head & (head << 1))) >> 1
  return not (row & result > 0)

def solution(g):
  rows = len(g)
  columns = len(g[0])
  # Rotate graph if needed, we want to apply CA on the short side
  if rows < columns:
    temp_g = [[] for _ in g[0]]
    for i in xrange(len(g)):
      for j in xrange(len(g[i])):
        temp_g[j].append(g[i][j])
    g = temp_g
    temp = rows
    rows = columns
    columns = temp
  # Transform graph into numbers to do binary calculation later.
  bin_g = []
  for row in g:
    temp = 0
    for gas in row:
      temp = temp << 1
      if gas: temp += 1
    bin_g.append(temp)
  # dp to keep track on the number that has already been visited
  dp = {}
  possible_heads = {i: 1 for i in xrange(1 << (columns + 1))}
  for bin_row in bin_g:
    possible_tails = {}
    for head in possible_heads:
      if not is_possible_head(columns, bin_row, head):
        continue
      tails = find_possible_tails(columns, bin_row, head, dp)
      for tail in tails:
        if tail not in possible_tails:
          possible_tails[tail] = 0
        possible_tails[tail] += possible_heads[head]
    possible_heads = possible_tails
  preimages = sum(possible_heads.values())
  # print(preimages)
  return preimages
