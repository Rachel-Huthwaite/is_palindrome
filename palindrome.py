def is_palindrome(s):

    last_index = len(s)-1
    line = len(s)//2
    
    for i in range(0, line):
        if s[i] != s [last_index]:
            return False
    return True