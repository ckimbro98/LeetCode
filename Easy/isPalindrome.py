class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        forward = []
        backward = []

        for i in s:
            if i.isalnum():
                backward.append(i)
                forward.insert(0, i)

        if forward == backward:
            return True
        
        return False

  ""
Time/Space Complexity: O(N)
  ""
