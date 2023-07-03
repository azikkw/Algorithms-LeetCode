def three_sum(nums):
    res = []

    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

    return res

print(three_sum([-1, 0, 1, 2, -1, -4]))
