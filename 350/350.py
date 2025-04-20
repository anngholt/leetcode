# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        result = []

        for num in count1:
            if num in count2:
                min_count = min(count1[num], count2[num])
                result.extend([num] * min_count)

        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 9, 5, 4]
    nums2 = [9, 4, 9, 8, 4]
    print(sol.intersect(nums1, nums2))  # Output can be [4, 4, 9] or [4, 9, 4]