def character_replacement(s, k):
    count = {}

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

    return (r - l + 1)

# My solution >>>
# def character_replacement(s, k): <<<< My solution
#     freq_map = {}
#     window, l = 0, 0
#
#     for r in range(len(s)):
#         freq_map[s[r]] = 1 + freq_map.get(s[r], 0)
#
#         while (r - l + 1) - max(freq_map.values()) > k:
#             freq_map[s[l]] -= 1
#             l += 1
#
#         window = max(window, r - l + 1)
#
#     return window


print(character_replacement("AAAA", 0))
