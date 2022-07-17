Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


Solution -


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        nums.sort()
        ans = []
        while(i < n):
            if(i == 0 or (i -1 >= 0 and nums[i] != nums[i-1])):
                firstElement = nums[i]
                target = 0 - firstElement
                pairs = self .twoSum(nums, i + 1, n - 1, target)
                for pair in pairs:
                    triplet = [firstElement, pair[0], pair[1]]
                    ans.append(triplet)
            i += 1

                
        return ans   
                               
    def twoSum(self, nums, start, end, target):
        f = start
        s = end
        pairs = []
        while (f < s ):
            if (f - 1 >= start and nums[f-1] == nums[f]):
                f = f + 1
                continue
            if  (s + 1 <= end and nums[s+1] == nums[s]):
                s = s - 1
                continue
            if (nums[f] + nums[s] < target):
                f += 1
            elif (nums[f] + nums[s] > target):
                s -= 1
            else:
                pair =[ nums[f], nums[s] ]
                pairs.append(pair)
                f +=1 
        return pairs        
            
