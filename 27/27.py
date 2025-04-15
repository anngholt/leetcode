class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range (len(nums)-1, -1, -1): # iterate backwards because we modify array in-place!
            if nums[i] == val:
                del nums[i]
        return len(nums)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3)) # return 2