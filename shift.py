def rotate(a):
    if not a:
        return a
    new_list = a[:]
    print(new_list)
    last_item = new_list[-1]
    for i in range(len(new_list)-1, 0, -1):
        new_list[i] = new_list[i-1]
    new_list[0] = last_item
    return new_list


a = [1, 2, 3]
print(rotate(a))