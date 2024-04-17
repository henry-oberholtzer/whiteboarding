# Two sorted arrays, nums1, nums2 sorted in non-decreasing order
# Two integers, m, n representing the number of elements in nums1 and nums2


def merge_sorted_array(nums1: list, nums2: list, m: int, n: int):
  if len(nums2) == 0:
    return
  for i in range(len(nums1)):
    if nums1[i] >= nums2[0] or nums1[i] == 0:
      nums1.insert(i, nums2[0])
      nums1.remove(0)
      merge_sorted_array(nums1, nums2[1:], m, n)
      break
  

if __name__ == "__main__":
  def example1():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    merge_sorted_array(nums1, nums2, m, n)
    expected = [1,2,2,3,5,6]
    print(nums1)
    print(nums1 == expected)
  def example2():
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    merge_sorted_array(nums1, nums2, m, n)
    expected = [1]
    print(nums1)
    print(nums1 == expected)
  def example3():
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    merge_sorted_array(nums1, nums2, m, n)
    expected = [1]
    print(nums1)
    print(nums1 == expected)
  example1()
  example2()
  example3()
