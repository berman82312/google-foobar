import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    entrances = [0]
    exits = [3]
    path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    self.assertEqual(solution.solution(entrances, exits, path), 6)

  def test2(self):
    entrances = [0, 1]
    exits = [4, 5]
    path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    self.assertEqual(solution.solution(entrances, exits, path), 16)

  def test3(self):
    entrances = [0, 1]
    exits = [5, 6]
    path = [
      [0, 0,10,10, 5, 0, 0],
      [0, 0,10,10, 5, 0, 0],
      [0, 0, 0, 0, 0,10,12],
      [0, 0, 0, 0, 0,18,10],
      [0, 0,10,10, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual(solution.solution(entrances, exits, path), 50)

  def test4(self):
    entrances = [0, 1]
    exits = [6, 7]
    path = [
      [0, 0,10,10, 5, 5, 0, 0],
      [0, 0,10,10, 5, 5, 0, 0],
      [0, 0, 0, 0, 0, 0,10,23],
      [0, 0, 0, 0, 0, 0,17,10],
      [0, 0,10,10, 0, 0, 0, 0],
      [0, 0,10, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual(solution.solution(entrances, exits, path), 60)

if __name__ == '__main__':
  unittest.main()
