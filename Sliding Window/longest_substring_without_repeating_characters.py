def length_of_longest_substring(s):
    char_set = set()
    l, res = 0, 0

    for c in range(len(s)):
        while s[c] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[c])
        res = max(res, c - l + 1)

    return res

print(length_of_longest_substring("abcabcbb"))
