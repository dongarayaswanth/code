
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        ptr = p1+p2 +1
        while p1>=0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[ptr] = nums1[p1]
                p1 -= 1
            else:
                nums1[ptr] = nums2[p2]
                p2 -= 1
            ptr -= 1
        while p2 >= 0:
            nums1[ptr] = nums2[p2]
            p2 -= 1
            ptr -= 1
        

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(solution.merge(nums1, m, nums2, n))
    print(nums1)  # Expected output: [1, 2, 2, 3, 5, 6]
    