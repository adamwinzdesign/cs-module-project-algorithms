'''
Input: an integer
Returns: an integer
'''

# cookie monster can eat either one, two, or three cookies at a time, but not four or more

# for memoization/caching, we need some sort of data structures, usually lists/arrays or dictionaries
# if we check the cache and find the answer we need, return it.
# if cache doesn't have what we're looking for, how do we get the answer added to the cache?

def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    # if cache exists, check it for the answer we need
    elif cache and cache[n] > 0:
        return cache[n]

    # init cache if it does not already exist
    else:
        if not cache:
            cache = [0 for _ in range(n + 1)]
        # now that the cache exists, we can save our answer
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]
    

def eating_cookies(n):
    # first pass solution:
    # base case: when there are no more cookies to eat:
    if n == 0:
        return 1
    # check for and prevent negative n values
    elif n < 0:
        return 0
    # represents eating one cookie
    # eating_cookies(n-1)

    # representing eating two cookies
    # eating_cookies(n-2)

    # representing eating three cookies
    # eating_cookies(n-3)

    # recursive case where there are still cookies to be eaten
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    # the above solution is not optimized because there is a lot of repeated work
    # we can use caching/memoization to speed up the runtime by enabling the algorithm to 'remember' the result of recursive calls that were already made, so that when it encounters a case that it has already seen, it can retrieve the result from the cache rather than calculating it again.


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
