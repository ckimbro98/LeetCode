class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        temp = ""

        for char in strs[0]:
            temp += char
            
            for string in strs:
                if not string.startswith(temp):
                    return prefix
                

            prefix = temp

        return prefix
