# My solution
def top_k_frequent(nums, k):
    frequencies = {}

    for i in nums:
        if i not in frequencies:
            frequencies[i] = []
        frequencies[i].append(i)

    res = []
    for i in sorted(list(frequencies.values()), key=len, reverse=True)[:k]:
        res.append(i[0])

    return res

nums = [5, 1, 1, 1, 2, 2]
k = 2

print(top_k_frequent(nums, k))


# Neetcode solution
def top_k_frequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        count[i] = 1 + count.get(i, 0)
    for i, j in count.items():
        freq[j].append(i)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
