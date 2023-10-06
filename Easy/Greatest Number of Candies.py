## First attempt - O(N^2) time complexity, very inefficient

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        mostCandy = True

        for i, candy in enumerate(candies):
            for j in candies:
                if candy + extraCandies < j:
                    result.append(False)
                    mostCandy = False
                    break

            if mostCandy:
                result.append(True)

            elif not mostCandy:
                mostCandy = True

            
        return result  

## Second attempt - O(N) time complexity, but for some reason runtime was slower lmao

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatestCandies = max(candies)
        for candy in candies:
            if candy + extraCandies >= greatestCandies:
                result.append(True)
                continue
            result.append(False)
        
        return result
