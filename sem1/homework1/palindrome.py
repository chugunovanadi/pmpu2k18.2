def palindrome(st):
    temp = st[::-1]
    return temp == st


s = str(input())
print(palindrome(s))
