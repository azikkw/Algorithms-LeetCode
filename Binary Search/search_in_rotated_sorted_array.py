def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        res = (l + r) // 2

        if nums[res] == target:
            return res
        elif nums[l] <= nums[res]:
            if target > nums[res] or target < nums[l]:
                l = res + 1
            else:
                r = res - 1
        else:
            if target < nums[res] or target > nums[r]:
                r = res - 1
            else:
                l = res + 1

    return -1

print(search([1, 3], 3))
