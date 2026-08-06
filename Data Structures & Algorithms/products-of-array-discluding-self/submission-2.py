class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre_num = 1
        for i in range(len(nums)):
            res[i] = pre_num
            pre_num = pre_num * nums[i]

        post_num = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * post_num
            post_num = post_num * nums[i]

        return res