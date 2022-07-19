Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


Solution -

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)
        return [left, right]
        
    def findLeft(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end :
            mid = (start+end)//2
            if (nums[mid] < target):
                start =  mid + 1
            elif (nums[mid] > target):               
                end = mid - 1
            else:
                ans = mid
                end = mid - 1
        return ans
    
    def findRight(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end :
            mid = (start+end)//2
            if (nums[mid] < target):
                start =  mid + 1
            elif (nums[mid] > target):               
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans
