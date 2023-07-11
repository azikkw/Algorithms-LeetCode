import math

def min_eating_speed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (r + l) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res

piles = [30,11,23,4,20]
h = 5

print(min_eating_speed(piles, h))