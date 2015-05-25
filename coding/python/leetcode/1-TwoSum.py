class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for ind,val in enumerate(nums):
            if val in d:
                return (d[val] + 1, ind + 1)

            d[target - val] = ind
        
        return (-1,-1)        

# test v1:
# In [25]: tt = range(0,32046,2)
# In [26]: %time test.twoSum(tt, 16021)
# CPU times: user 3.72 s, sys: 6.2 ms, total: 3.72 s
# Wall time: 3.72 s
# Out[26]: (-1, -1)

#version 2:
# %time test.twoSum(tt, 16021)
# CPU times: user 3.8 ms, sys: 1.62 ms, total: 5.42 ms
# Wall time: 4.09 ms
# Out[50]: (-1, -1)

test=Solution()
#test.twoSum(range(0,32046,2), 16021)                
result = test.twoSum([2,3,4,5],6)                
