def search_matrix(matrix, target):
    for m in matrix:
        l, r = 0, len(m) - 1
        while l <= r:
            res = l + int((r - l) / 2)
            if m[res] == target:
                return True
            elif m[res] < target:
                l = res + 1
            else:
                r = res - 1

    return False
