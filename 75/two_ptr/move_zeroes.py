"""
Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""
def move_zeroes(nums):
    # Pointer to track the position of the next non-zero element
    non_zero = 0

    # Traverse the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the current element with the position of the non-zero pointer
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1
            print(nums)
            print("*"*100)

# Example usage
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]