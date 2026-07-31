class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lengths1 = len(t)
        lengths2 = len(s)
        maxi = lengths2-lengths1
        mint=1001
        ans = ""
        for letter in range(lengths2):
            if letter > maxi:
                return ans
            else:
                if s[letter] in t:
                    temp = ''
                    string1 = t
                    for first in range(lengths2-letter):
                        temp += s[letter+first]
                        if s[letter+first] in string1:
                            string1 = string1.replace(s[letter+first],'',1)
                        if  string1 == '':
                            if mint > len(temp):
                                mint = len(temp)
                                ans = temp
                            break
                            
                            
        return ans
                    
