class Solution:
    def isValid(self, s: str) -> bool:
        closed = []
        bracketDict = {']':'[', ')':'(', '}':'{'}
        for i in s:

            if i == '(' or i == '[' or i == '{':
                closed.append(i)
                continue

            #Checking close brackets
            if len(closed) == 0:
                return False

            endBracket = closed.pop()
            if endBracket != bracketDict[i]:
                return False
        if len(closed) > 0:
                return False
        return True
"""
( ??? )
[ ??? ]
{ ??? }
"""
