# 7. Maximum Subarray
#    - Write a program to find the maximum sum of a contiguous subarray within a given array.
#    - Expected output: If the input array is `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the output should be `6`, as the maximum subarray is `[4, -1, 2, 1]`.



def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(input_array)
print(result)
