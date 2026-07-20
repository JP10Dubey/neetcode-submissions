class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        currentLength = 0
        subStr = []
        strlen = len(s)
        for i in range(strlen):
            if maxlength< (strlen-i):
                while (i!=strlen) and (s[i] not in subStr):
                    subStr.append(s[i])
                    i+=1
                maxlength = max(maxlength,len(subStr))
                subStr = []
            else:
                return maxlength
        return maxlength