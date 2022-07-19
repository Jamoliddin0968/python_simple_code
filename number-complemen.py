class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        bin_num = list(map(lambda x: 0 if x == '1' else 1,bin_num))
        res = 0 
        for x in bin_num:
            res = res*2+x
        return res