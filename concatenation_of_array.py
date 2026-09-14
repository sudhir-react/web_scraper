from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(3):
            for n in nums:
                ans.append(n)

        return ans

# Create object
solution = Solution()

# Call the function
result = solution.getConcatenation([1, 2, 1])

print(result)