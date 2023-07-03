def is_valid(s):
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for i in s:
        if i not in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False
