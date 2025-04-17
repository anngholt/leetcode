class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for n in nums:
            result ^= n
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([1,2,3,4,2,3,5,7,5,1,4])) # out: 7