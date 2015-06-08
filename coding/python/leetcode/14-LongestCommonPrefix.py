#Longest Common Prefix
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        s = ""
        nStr = len(strs)
        if nStr < 1: return s
        if nStr == 1: return strs[0]
        if len(strs[0]) == 0: return s
        
        for i in range(len(strs[0])):        	
        	c = strs[0][i]        	  
        	for j in range(1,nStr):
        		if ((i >= len(strs[j])) or (c != strs[j][i])):
        			return s
        		s = s + c
        return s		


a= Solution()
print a.longestCommonPrefix(['a','a'])        			


