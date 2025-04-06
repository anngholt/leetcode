class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(-121))  # Output: false
    print(sol.isPalindrome(121))  # Output: true
        
#   Time Complexity: O(log(n)) -- only half the digits are processed
#   Space Complexity: O(1) --  no strings, no extra memory used
