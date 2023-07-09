def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        res = l + int((r - l) / 2)

        if nums[res] == target:
            return res
        elif nums[res] < target:
            l = res + 1
        else:
            r = res - 1

    return -1
