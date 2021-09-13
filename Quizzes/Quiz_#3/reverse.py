def inverte(s):
    if s == '':
        return ''
    else:
        return s[-1] + inverte(s[:-1])


s = input()
print(inverte(s))
