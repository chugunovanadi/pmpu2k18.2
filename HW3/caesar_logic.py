def encrypt(offset, text):
    res = []
    for i in text:
        if not (65 <= ord(i) <= 90) and not (97 <= ord(i) <= 122):
            res.append(i)
        else:
            if 97 <= ord(i) <= 122:
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

            if 65 <= ord(i) <= 90:
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
    res = []
    for i in text:
        if not (65 <= ord(i) <= 90) and not (97 <= ord(i) <= 122):
            res.append(i)
        else:
            if 97 <= ord(i) <= 122:
                n = ord(i) - offset
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

            if 65 <= ord(i) <= 90:
                n = ord(i) - offset
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
