def check_inclusion(s1, s2):
    cnt = 0

    for i in range(len(s1)):
        for j in range(i + 1, len(s2)):
            if s1[i] == s2[j]:
                if len(s2) - j == 1 and s1[i + 1] == s2[j + 1]:
                    cnt += 2

    return cnt

print(check_inclusion("ab", "eidbaooo"))
