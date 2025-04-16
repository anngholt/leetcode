class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        len_hay = len(haystack)
        len_nee = len(needle)

        for i in range(0, len_hay - len_nee + 1):
            if haystack[i:i + len_nee] == needle:
                return i     
        return - 1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad")) # returns 0
    print(sol.strStr("leetcode", "leeto")) # returns -1