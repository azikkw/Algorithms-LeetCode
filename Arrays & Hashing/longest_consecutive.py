def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for i in nums:
        if (i - 1) not in num_set:
            length = 0
            while (i + length) in num_set:
                length += 1
            longest = max(length, longest)

    return longest

print(longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
