import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    test_input = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
    self.assertEqual(solution.solution(test_input, 1), [1, 2])

  def test2(self):
    test_input = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    self.assertEqual(solution.solution(test_input, 3), [0, 1])

  def test3(self):
    test_input = [
      [0,  1,  5,  5,  2],
      [10, 0,  2,  6,  10],
      [10, 10, 0,  1,  5],
      [10, 10, 10, 0,  1],
      [10, 10, 10, 10, 0]]
    self.assertEqual(solution.solution(test_input, 5), [0, 1, 2])

  def test4(self):
    test_input = [
      [0,-1, 0, 9, 9, 9, 9, 9],  # Start
      [9, 0, 1, 9, 9, 9, 9, 9],  # 0
      [0, 9, 0, 0, 9, 9, 1, 1],  # 1
      [9, 9, 9, 0, 1, 9, 9, 9],  # 2
      [9, 9, 9, 9, 0,-1, 9, 9],  # 3
      [9, 9, 0, 9, 9, 0, 9, 9],  # 4
      [9, 9,-1, 9, 9, 9, 0, 9],  # 5
      [9, 9, 9, 9, 9, 9, 9, 0]] # bulkhead
    self.assertEqual(solution.solution(test_input, 1), [0, 1, 2, 3, 4, 5])

  def test5(self):
    test_input = [
      [0, 1, 3, 4, 2],
      [10, 0, 2, 3, 4],
      [10, 10, 0, 1, 2],
      [10, 10, 10, 0, 1],
      [10, 10, 10, 10, 0]]
    self.assertEqual(solution.solution(test_input, 4), [])

  def test6(self):
    test_input = [
      [1, 1, 1, 1, 1],
      [-1, 1, 1, 1, 1],
      [-1, 1, 1, 1, 1],
      [-1, 1, 1, 1, 1],
      [-1, 1, 1, 1, 1]]
    self.assertEqual(solution.solution(test_input, 1), [0, 1, 2])

  def test7(self):
    test_input = [
      [0, 90,90,90,90],
      [90, 0,-1,90,90],
      [90,-1, 0,90,90],
      [90,90,90, 0,90],
      [90,90,90,90, 0]]
    self.assertEqual(solution.solution(test_input, 1), [0, 1, 2])

  def test8(self):
    test_input = [
      [0, 0],
      [0, 0]]
    self.assertEqual(solution.solution(test_input, 1), [])

  def test9(self):
    test_input = [
      [0, 20, 20, 20, -1],
      [90, 0, 20, 20, 0],
      [90, 30, 0, 20, 0],
      [90, 30, 20, 0, 0],
      [-1, 30, 20, 20, 0]]
    self.assertEqual(solution.solution(test_input, 0), [0, 1, 2])

  def test10(self):
    test_input = [
      [0, 1, 1, 1, 1],
      [1, 0, 1, 1, 2],
      [1, 1, 0, 1, 1],
      [1, 1, 1, 0, 3],
      [1, 1, 1, -2, 0]]
    self.assertEqual(solution.solution(test_input, 1), [1, 2])

if __name__ == '__main__':
  unittest.main()
