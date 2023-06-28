def two_sum(nums, target):
    h_set = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                h_set.add(i)
                h_set.add(j)
                return h_set

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
