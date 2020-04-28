def remove_char_at(str, n):
    x = 0
    copystr = ""
    for i in str:
        if x != n:
            copystr += i
        x += 1
    return (copystr)
