# def check_inclusion(s1, s2): My try
#     res = {}
#
#     if len(s1) > len(s2):
#         return False
#
#     for i in range(len(s1)):
#         res[s1[i]] = ""
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 res[s1[i]] += str(j)
#
#     cnt = 0
#     ans = set()
#
#     for i in res.values():
#         for j in i:
#             ans.add(j)
#
#     ans = sorted(list(ans))
#     print(ans)
#
#     for i in range(len(ans)):
#         for j in range(i + 1, len(ans)):
#             if int(ans[j]) - int(ans[i]) == 1:
#                 cnt += 1
#
#     return True if len(ans) - cnt == 1 else False

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1

    return matches == 26

print(check_inclusion("hello", "ooolleoooleh"))
