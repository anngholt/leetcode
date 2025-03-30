class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k > n
        
        # Reverse the entire array
        nums.reverse()
        
        # Reverse the first k elements properly
        nums[:k] = list(reversed(nums[:k]))
        
        # Reverse the remaining elements properly
        nums[k:] = list(reversed(nums[k:]))

# Ensure this only runs when the script is executed directly
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Initial array: ", nums, "rotation factor: ", k)
    Solution().rotate(nums, k)
    print("Rotated array: ", nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
