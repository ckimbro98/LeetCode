class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = ""

        for i in range(len(s)):
            if s[i] != " ":
                lastWord += s[i]

            else:
                if i < len(s) - 1 and s[i + 1] != " ":
                    lastWord = ""


        return len(lastWord)

        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
