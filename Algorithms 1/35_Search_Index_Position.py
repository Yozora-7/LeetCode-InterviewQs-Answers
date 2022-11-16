"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Log(N)
        l, r = 0, len(nums) - 1 

        while l <= r: # while the left is less than or equal to the right
            mid = (l + r) // 2 # find the middle position

            if target == nums[mid]: # if the target is at the middle position, return it
                return mid
            
            if target > nums[mid]: # if the target is greater than the middle, go from the
                l = mid + 1 #        left onwards
            
            else: # else, the target can only be at the right position
                r = mid - 1
        
        return l # return the left position
