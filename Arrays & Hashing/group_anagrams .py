def group_anagrams_second(strs):
    group = {}  # creation of a hash set

    for i in strs:
        sorted_str = ''.join(sorted(i))  # sorted string
        # print(sorted_str)

        if sorted_str not in group:
            group[sorted_str] = []  # creating key of string and its values
        group[sorted_str].append(i)  # append values to this key
        # print(group)

    return list(group.values())

print(group_anagrams_second(["eat", "tea", "tan", "ate", "nat", "bat"]))
