# First solution: two for loops, complexity of O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        sum = []
        length = len(nums)
  
        for i in range(length):
            for j in range(i + 1, length):
                addTarget = nums[i] + nums[j]
                if addTarget == target:
                    sum.append(i)
                    sum.append(j)
                    return sum

# Second solution: create dict, complexity of O(n)
class Solution(object):
    def twoSum(self, nums, target):
        sum = {}
        length = len(nums)

        for i in range(length):
            addend = target - nums[i]
            if addend in sum:
                return [sum[addend], i]
            
            sum[nums[i]] = i

        return None
