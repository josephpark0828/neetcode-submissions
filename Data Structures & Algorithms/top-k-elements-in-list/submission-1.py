class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap that contains each element and its count
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # format it to be in [ , ] form
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        arr.sort()

        # return the k most frequent elements
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res