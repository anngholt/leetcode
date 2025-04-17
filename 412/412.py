class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        str_array = [] 

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                str_array.append("FizzBuzz")
            elif i % 3 == 0:
                str_array.append("Fizz")
            elif i % 5 == 0:
                str_array.append("Buzz")
            else:
                str_array.append(str(i))
        return str_array


if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(15))  # out: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
