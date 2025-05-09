class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                count += 1
            else:
                num = num - 1
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSteps(14)) #out: 6