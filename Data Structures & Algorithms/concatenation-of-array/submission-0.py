class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)

        for actual in nums:
            ans.append(actual)

        return ans