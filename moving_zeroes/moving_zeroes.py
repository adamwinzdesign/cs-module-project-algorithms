'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeros_absent = [elem for elem in arr if elem != 0]
    number_of_zeros = len(arr) - len(zeros_absent)
    zeros_absent.extend([0] * number_of_zeros)
    return zeros_absent


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")