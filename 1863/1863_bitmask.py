class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.total = 0  # To store the sum of XORs
        n = len(nums)
        
        # Iterate over all possible bitmasks (0 to 2^n - 1)
        for mask in range(1 << n):
            current_xor = 0
            # Check each bit position
            for i in range(n):
                if mask & (1 << i):  # If i-th bit is set, include nums[i]
                    current_xor ^= nums[i]
            self.total += current_xor
        
        return self.total

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetXORSum([1, 3]))  # Output: 6
    print(sol.subsetXORSum([5, 1, 6]))  # Output: 28