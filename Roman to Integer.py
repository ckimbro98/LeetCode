class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        prev_value = 0
        
        for i in range(len(s)):
            value = romanNums[s[i]]
            
            if i > 0 and value > prev_value:
                # Subtract the value of the previous numeral (2 * prev_value)
                integer += value - 2 * prev_value
            else:
                integer += value
            
            prev_value = value
        
        return integer
