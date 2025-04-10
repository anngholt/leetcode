class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
if __name__ == "__main__":
    nums = [1,2,3,1]
    sol = Solution()
    print("Output: ", sol.containsDuplicate(nums))