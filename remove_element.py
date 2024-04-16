# Given an integery array nums1 and an int val
# remove all occurences of val in nums, in place
# return number of elements in nums not equal to val


def remove_element(nums: list, val: int):
  filtered = [i for i in nums if i != val]
  nums[:] = filtered
  return len(filtered)

if __name__ == "__main__":
  def example1():
    nums = [3,2,2,3]
    val = 3
    output = 2
    expected = [2,2,]
    print(nums, val)
    print(remove_element(nums, val) == output)
    print(nums, val)
    print(nums == expected)
  def example2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    output = 5
    expected = [0,1,4,0,3]
    print(nums, val)
    print(remove_element(nums, val) == output)
    print(nums, val)
    print(nums == expected)
  example1()
  example2()
