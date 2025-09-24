#https://leetcode.com/problems/palindrome-number/submissions/1781622183/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = False
        holder = ''
        if str(x)[::-1] == str(x):
            answer = True
        return answer

s=Solution()
print(s.isPalindrome(7987))
