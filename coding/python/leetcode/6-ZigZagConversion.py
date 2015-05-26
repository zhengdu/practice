class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1: return s
        out = ['' for i in range(numRows)]
        direct = 1
        move = -1
        for ind,val in enumerate(s):           
            if move == (numRows -1):
                direct = -1 
            elif move == 0:
        		direct = 1	 
       
            move = move + direct
            out[move] += val

        return ('').join(out)			



a= Solution()
print a.convert('abcdefghij',4)
