#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        ctr = 0
        skipper = 0
        answer = 0
        for i in s:
            print(i)
            if ( (ctr < skipper )):
                ctr +=1
                print('this worked')
                continue
            if (s[ctr:ctr+2] in roman_map):
                answer += roman_map[s[ctr:ctr+2]]
                skipper += 1
                print(s[ctr:ctr + 2])

            else:
                answer += roman_map[i]
            ctr +=1
            skipper +=1
        return (answer)
s = Solution()
print(s.romanToInt('MCMXCIV'))