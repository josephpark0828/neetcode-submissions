class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float("-infinity")

            if (i + 1) < len(A):
                Aright = A[i + 1]
            else:
                Aright = float("infinity")

            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = float("-infinity")

            if (j + 1) < len(B):
                Bright = B[j + 1]
            else:
                Bright = float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    if Aright < Bright:
                        return Aright
                    else:
                        return Bright
                else:
                    if Aleft > Bleft:
                        max_left = Aleft
                    else:
                        max_left = Bleft

                    if Aright < Bright:
                        min_right = Aright
                    else:
                        min_right = Bright

                    return (max_left + min_right) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
