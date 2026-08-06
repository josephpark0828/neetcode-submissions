class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preVal = set()

        for n in nums:
            if n in preVal:
                return True
            preVal.add(n)
        return False