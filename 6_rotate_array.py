import unittest
# Given an integer array nums, rotate the array to the right by k steps
# k is non-negative

def rotate_array(nums: list, k: int):
  for _ in range(k):
    item = nums.pop()
    nums.insert(0, item)
  return nums

class TestRemoveDuplicates(unittest.TestCase):
  def test_example1(self):
    nums = [1,2,3,4,5,6,7]
    expected = [5,6,7,1,2,3,4]
    result = rotate_array(nums, 3)
    self.assertEqual(result, expected)
  def test_example2(self):
    nums = [-1,-100,3,99]
    expected = [3,99,-1,-100]
    result = rotate_array(nums, 2)
    self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()
