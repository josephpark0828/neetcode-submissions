class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1
        while True:
            mA = (l + r) // 2
            mB = half - mA - 2

            if mA < 0:
                leftA = float("-inf")
            else:
                leftA = A[mA]

            if (mA + 1) >= len(A):
                rightA = float("inf")
            else:
                rightA = A[mA + 1]
            
            if mB < 0:
                leftB = float("-infinity")
            else:
                leftB = B[mB]

            if (mB + 1) >= len(B):
                rightB = float("inf")
            else:
                rightB = B[mB + 1]
            
            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = mA - 1
            else:
                l = mA + 1


