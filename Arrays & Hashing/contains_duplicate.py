def contains_duplicate(nums):
    hset = set()
    for i in nums:
        if i in hset:
            return True
        else:
            hset.add(i)

answer = contains_duplicate([1, 2, 3, 1])
print(answer)