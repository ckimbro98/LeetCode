class Solution(object):
    def mergeAlternately(self, word1, word2):
        merge = []
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merge.append(word1[i])
            if i < len(word2):
                merge.append(word2[i])
            i += 1
        
        return ''.join(merge)

        """
        Time complexity: O(n), where n is the length of the longer string
        Space complexity: O(n), where n is the length of the longer string

        """
