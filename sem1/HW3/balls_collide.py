def balls_collide(arg1, arg2):
    distance_cent = ((arg1[0] - arg2[0]) ** 2 + (arg1[1] - arg2[1]) ** 2) ** 0.5
    if arg1[2] < 0 or arg2[2] < 0:
        raise Exception("Отрицательный радиус")
    return True if distance_cent <= arg1[2] + arg2[2] else False
