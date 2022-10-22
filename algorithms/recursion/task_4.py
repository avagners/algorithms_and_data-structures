def is_palidrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palidrome(s[1:-1])
    else:
        return False
