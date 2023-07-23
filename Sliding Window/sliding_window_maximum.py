def max_sliding_window(nums, k):
    res = []

    for i in range(len(nums)):
        if len(nums) - i >= k:
            res.append(max(nums[i:(k + i)]))

    return res

# def maxSlidingWindow(self, nums, k): <- NeetCode Solution
#     output = []
#     q = collections.deque()  # index
#     l = r = 0
#
#     # O(n) O(n)
#     while r < len(nums):
#         # pop smaller values from q
#         while q and nums[q[-1]] < nums[r]:
#             q.pop()
#         q.append(r)
#
#         # remove left val from window
#         if l > q[0]:
#             q.popleft()
#
#         if (r + 1) >= k:
#             output.append(nums[q[0]])
#             l += 1
#         r += 1
#
#     return output

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(max_sliding_window([1], 1))
