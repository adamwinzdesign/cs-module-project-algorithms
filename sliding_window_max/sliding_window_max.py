'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    result_arr = []

    pointer_lo = 0
    pointer_hi = k - 1
    while pointer_hi != len(nums):
        window_vals = nums[pointer_lo:pointer_hi + 1] # here + 1 because of the split
        window_max = max(window_vals)
        pointer_lo += 1
        pointer_hi += 1
        result_arr.append(window_max)

    return result_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
