import unittest
import solution

class SolutionTest(unittest.TestCase):
  def test1(self):
    self.assertEqual('9', solution.solution(3, 2))

  def test2(self):
    self.assertEqual('96', solution.solution(5, 10))

  def test3(self):
    self.assertEqual('1', solution.solution(1, 1))

  def test4(self):
    self.assertEqual('169444612', solution.solution(8176, 10234))

  def test5(self):
    self.assertEqual('5317231251', solution.solution(3125, 100000))

  def test6(self):
    self.assertEqual('19999800001', solution.solution(100000, 100000))

  def test7(self):
    self.assertEqual('4980069901', solution.solution(1,99801))

  def test8(self):
    self.assertEqual('4980269502', solution.solution(99801,2))

if __name__ == '__main__':
  unittest.main()
