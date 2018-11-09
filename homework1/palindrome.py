def palindrome(str):
    temp = str[::-1]
    return temp == str


s = str(input())
print(palindrome(s))
