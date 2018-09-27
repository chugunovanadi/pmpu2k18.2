def rotate(a):
    try:
        tmp = a[len(a)-1]
        for i in range(len(a)-1, 0, -1):
            a[i] = a[i-1]
        a[0] = tmp
    except IndexError:
        print("Массив пуст")


a = []
rotate(a)
print(a)
