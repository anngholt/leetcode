class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
if __name__ == "__main__":
    nums = [1,2,3,1]
    sol = Solution()
    print("Output: ", sol.containsDuplicate(nums))