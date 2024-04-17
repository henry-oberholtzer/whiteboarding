import unittest
# Given an integer array nums of size n, return the majority element
# The majority element appears more than n/2 times.
# The majority element can always be assumed to exist.

def majority_element(nums: list):
  majority = (0, None)
  for num in nums:
    if nums.count(num) > majority[0]:
      majority = (0, num)
  return majority[1]

class TestRemoveDuplicates(unittest.TestCase):
  def test_example1(self):
    nums = [3,2,3]
    expected = 3
    result = majority_element(nums)
    self.assertEqual(result, expected)
  def test_example2(self):
    nums = [2,2,1,1,1,2,2]
    expected = 2
    result = majority_element(nums)
    self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()
