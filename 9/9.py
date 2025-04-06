class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]  #not the most efficient, but super easy one-line solution

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(-121))  # Output: false
    print(sol.isPalindrome(121))  # Output: true
        
#   Time Complexity: O(n)
#   Space Complexity: O(n) (for storing the string and its reversed copy)
