class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = set()

        for actual in nums:
            if actual in array:
                return True

            array.add(actual)

        return False
        