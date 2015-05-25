class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        
        for ind,val in enumerate(nums):
            diff = target - val
            ind2 = nums.index(diff) if (diff in nums) else -1
            if ind2 == -1 & ind > len(nums)/2:
                break
            elif ind2 != -1:
                return (ind+1,ind2+1)

        return (-1,-1)        


test=Solution()
test.twoSum(range(0,32046,2), 16021)                