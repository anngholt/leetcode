class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            # If even (last bit 0), one step to shift
            # If odd (last bit 1), one to subtract, one to shift next
            if num & 1 == 0:  # Is even: by using bitwise AND with 001
                num >>= 1     # Right shift num by 1 bit (bitwise shifting)
            else:
                num -= 1
            steps += 1
        return steps

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSteps(14)) #out: 6