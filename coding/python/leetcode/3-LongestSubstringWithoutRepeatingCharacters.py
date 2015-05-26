class Solution:
    # @param {string} s
    # @return {integer}

    #v1: Status: Time Limit Exceeded
	#CPU times: user 4.34 ms, sys: 1.46 ms, total: 5.81 ms
	#Wall time: 4.49 ms
    # def lengthOfLongestSubstring(self, s):
    # 	longest = 0
    # 	for i in range(0,len(s)-1):
    # 		for j in range(1,len(s)):
    # 			if len(set(s[i:j])) < len(s[i:j]):
    # 				break
    # 			else:
    # 				longest = len(s[i:j]) if longest < len(s[i:j]) else longest
    # 	return longest

    def lengthOfLongestSubstring(self, s):
        res = 0
        cur = 0
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                cur += 1
            else:
                cur = min(i - d[c], cur + 1)
            d[c] = i
            res = max(res, cur)
            print i,c            
            print d
            print res, cur
        return res



a = Solution()
#print a.lengthOfLongestSubstring('cmlzejecnokgdadvlloihqnbnusaosusgfsmoyrdodjrdmmozcyhulijgajwueodlipchgfxkrpnfdeficocowmwy')    					
print a.lengthOfLongestSubstring('pwwkew')