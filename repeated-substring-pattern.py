class Solution:
    """for leetcode problems
    """
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len = len(s)
        temp = ""
        
        for i in range(s_len):
            temp+=s[i]
            # print("temp",temp)
            if i+1> s_len//2:
                return False
            if i==0 or s_len%(i+1)!=0:
                continue
            j , step = i+1 , i+1

            n = True
            while j < s_len:
                b= s[j:(step+j)]
                # print("b=",b)
                if temp != b:
                    n = False
                j += step
            if n:
                return  True
        return True