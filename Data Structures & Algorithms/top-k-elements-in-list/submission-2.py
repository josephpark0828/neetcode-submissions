class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap that contains each of the numbers and their counts
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        arr = []
        for num, cnt in counts.items():
            arr.append([cnt, num])

        arr.sort()

        #find the k elements that are the most frequent
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
