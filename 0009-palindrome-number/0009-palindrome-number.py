class Solution:
    def isPalindrome(self, x):
        x = str(x)

        if x == x[::-1]:
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(121))