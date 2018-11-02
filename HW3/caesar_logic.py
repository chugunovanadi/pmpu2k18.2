def encrypt(offset, text):
    res = []
    if offset > 25 or offset < -25:
        raise Exception("Ошибочное смешение")
    for i in text:
        if (not (ord('A') <= ord(i) <= ord('Z')) and
                not (ord('a') <= ord(i) <= ord('z'))):
            res.append(i)
        else:
            if ord('a') <= ord(i) <= ord('z'):
                n = ord(i) + offset
                if n > ord('z'):
                    n = n - ord('z') + ord('a') - 1
                    char = chr(n)
                    res.append(char)
                elif n < ord('a'):
                    n = ord('z') - ord('a') + n + 1
                    char = chr(n)
                    res.append(char)
                else:
                    char = chr(n)
                    res.append(char)
            if ord('A') <= ord(i) <= ord('Z'):
                n = ord(i) + offset
                if n > ord('Z'):
                    n = n - ord('Z') + ord('A') - 1
                    char = chr(n)
                    res.append(char)
                elif n < ord('A'):
                    n = ord('Z') - ord('A') + n + 1
                    char = chr(n)
                    res.append(char)
                else:
                    char = chr(n)
                    res.append(char)
    return ''.join(res)


def decrypt(offset, text):
    return encrypt(-offset, text)
