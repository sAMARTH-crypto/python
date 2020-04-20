#maximum sub array

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
         
        total_sum = max_sum = nums[0]    #current value of total & max sum is the value at 0th index
        
        for i in nums[1:]:               #iterating over list from 1st index
            
            total_sum = max(i,total_sum+i)              #total sum is maximum value of i,sum of i+prev values sum
            max_sum = max(max_sum,total_sum)        
            
        return max_sum
