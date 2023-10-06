class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxJump = 0
      
        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
          
        return True

  """
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
  """
