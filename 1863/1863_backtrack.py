class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.total = 0  # To store the sum of XORs

        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return
            # Include nums[index] in XOR
            dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index]
            dfs(index + 1, current_xor)

        dfs(0, 0)
        return self.total
if __name__ == "__main__":
    nums = [5,1,6]
    sol = Solution()
    print("OUTPUT: ", sol.subsetXORSum(nums))

