from math import sqrt


def dividers(n):
    ans = []
    for (i) in range(1, int(sqrt(abs(n)))+1):
        if abs(n) % i == 0:
            ans.append(i)
            ans.append(-i)
            ans.append(int(n/i))
            ans.append(int(-n / i))
    ans.sort()
    return ans


if __name__ == "__main__":
    n = int(input())
    print(dividers(n))