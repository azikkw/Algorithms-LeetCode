def is_anagram(s, t):
    if len(s) != len(t):
        return False

    for i in set(s):
        if s.count(i) != t.count(i):
            return False

    return True


def is_anagram_second(s, t):
    new_s = sorted(s)
    new_t = sorted(t)
    return True if new_s == new_t else False


print(is_anagram("anagram", "nagaram"))
print(is_anagram_second("anagram", "nagaram"))
