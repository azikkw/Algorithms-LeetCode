def max_area(height):
    left, right = 0, len(height) - 1
    res = 0

    while left < right:
        sum = (right - left) * min(height[left], height[right])
        res = max(sum, res)

        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return res
