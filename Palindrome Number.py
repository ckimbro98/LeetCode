class Solution:
    def isPalindrome(self, x: int) -> bool:
        intstring = str(x)
        for i in range(len(intstring)):
            if intstring[i] != intstring[len(intstring) - 1 - i]:
                return False

        return True
