from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                st.append(s[i])
            elif not st: 
                return False
            elif s[i] == ")":  
                if st[-1] == "(":
                    st.pop()
                else:
                    return False
            elif s[i] == "}":  
                if st[-1] == "{":
                    st.pop()
                else:
                    return False
            elif s[i] == "]":  
                if st[-1] == "[":
                    st.pop()
                else:
                    return False
        return False if st else True