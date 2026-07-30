class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1 = s1
        lengths1 = len(s1)
        lengths2 = len(s2)
        maxi = lengths2-lengths1
        for letter in range(lengths2):
            if letter > maxi:
                return False
            else:
                if s2[letter] in s1:
                    for first in range(lengths1):
                        if s2[letter+first] in string1:
                            string1 = string1.replace(s2[letter+first],'',1)
                        else:
                            break
                    if  string1 == '':
                        return True
                    else:
                        string1 = s1
        return False
                    
