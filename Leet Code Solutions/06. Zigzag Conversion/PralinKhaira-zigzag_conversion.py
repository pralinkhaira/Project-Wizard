class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<3 or numRows == 1:
            return s
        l = []
        n = 2*numRows-2
        for i in range(numRows):
            k=i
            c = 1 
            while k < len(s):
                l.append(s[k])
                if c%2 == 0 and i != 0:
                    k += (2*i)
                elif c%2 == 1 and i != numRows-1:
                    k += (n-(2*i))
                else:
                    k += n
                c += 1

        return ''.join(l)
