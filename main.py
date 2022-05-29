def brackets(q):
    i = 0
    a = 0

    while i != len(q) and a >= 0:
        if q[i] == '(':
            a += 1
        elif q[i] == ')':
            a -= 1
        i += 1

    if a == 0:
        return True
    else:
        return False


s = input()
print(brackets(s))
