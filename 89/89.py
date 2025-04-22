class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        # Total 2^n values in Gray code sequence
        for i in range(1 << n):  # same as 2 ** n
            gray = i ^ (i >> 1)  # Gray code formula
            result.append(gray)

        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 2
    print("Gray code sequence for n = {}:".format(n), sol.grayCode(n))
