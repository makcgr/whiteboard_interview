﻿var nums = new int[] {4,5,6,7,0,1,2};
var target = 0;
var result = Search(nums, target);

int Search(int[] nums, int target)
{
    int left = 0, right = nums.Length - 1;
    
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target)
            return mid;
            
        if (nums[left] <= nums[mid])
        {
            if (target >= nums[left] && target < nums[mid])
                right = mid - 1;
            else
                left = mid + 1;
        }
        else
        {
            if (target > nums[mid] && target <= nums[right])
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    return -1;
}
