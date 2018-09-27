from dividers import dividers


def is_prime(n):
    if n == 1:
        return True
    return len(dividers(n)) == 2


n = int(input())
print(is_prime(n))
