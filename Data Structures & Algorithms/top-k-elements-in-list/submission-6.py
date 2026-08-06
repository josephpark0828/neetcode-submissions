class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = {}
        for num in nums:
            counts_dict[num] = counts_dict.get(num, 0) + 1
        
        freq_buckets = []
        for i in range(len(nums) + 1):
            freq_buckets.append([])
        for num, cnt in counts_dict.items():
            freq_buckets[cnt].append(num)
        
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res