'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):  #O(n^2)
    # Your code here
    encountered = {}
    for elem in range(len(arr)):
        if arr[elem] in encountered:
            del encountered[arr[elem]]
        else:
            encountered[arr[elem]] = arr[elem]
    return next(iter(encountered.values()))

# first pass from lecture:
def single_number_with_array(nums):
    # set up an array to hold numbers we've already seen
    # check to see if the number is already in the array
    no_dups = []
    for x in nums: #O(n)
        if x not in no_dups:  #O(n)
            no_dups.append(x)
        else:
            no_dups.remove(x)  #O(n)
    return no_dups[0]

# another example from lecture, O(2 * n) ~ O(n)
def single_number(nums):
    # keep track of counts of how many times we have seen a number
    # dictionaries are better at being searched
    counts = {}

    # loop through numbs to tally how many times we've seen each number
    for x in nums: #O(n)
        if x in counts: #O(1)  This is O(1) instead of O(n) as above
            # if x is already in counts, increment the count by 1
            counts[x] += 1
        else:
            # if x is not already in counts, add it and set the count to 1
            counts[x] = 1
    
    # loop through the key:value pairs in counts to find the pair whose value is 1 to determine the odd number out.  Each other pair should have a value of 2
    for num in counts: #O(n)  We have two O(n) but they are not nested
        if counts[num] == 1
            return num

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
