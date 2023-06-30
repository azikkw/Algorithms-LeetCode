def is_palindrome(s):
    res = ""
    for i in s.lower():
        if i.isdigit() or 'a' <= i <= 'z':
            res += i

    return res == ''.join(reversed(res))

print(is_palindrome("A man, a plan, a canal: Panama"))
