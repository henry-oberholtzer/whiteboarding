import unittest
# Given an integer array nums sorted in non-decreasing order, remove the duplicates *in place* such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Return the number of unique elements in nums.

def remove_duplicates(nums: list):
  output_list = []
  for num in nums:
    if output_list.count(num) != 2:
      output_list.append(num)
  nums[:] = output_list
  return len(nums)

class TestRemoveDuplicates(unittest.TestCase):
  def test_example1(self):
    nums = [1,1,1,2,2,3]
    expected = [1,1,2,2,3,]
    result = remove_duplicates(nums)
    self.assertEqual(result, len(nums))
    self.assertEqual(expected, nums)
  def test_example2(self):
    nums = [0,0,1,1,1,1,2,3,3]
    expected = [0,0,1,1,2,3,3,]
    result = remove_duplicates(nums)
    self.assertEqual(result, len(nums))
    self.assertEqual(expected, nums)

if __name__ == '__main__':
  unittest.main()
