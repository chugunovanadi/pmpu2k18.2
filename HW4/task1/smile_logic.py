def smile(text):
    sad_sm = ('(', '[', '{')
    happy_sm = (')', ']', '}')
    res = []
    for i in text:
        if i in sad_sm:
            res.append(i)
        if i in happy_sm:
            if len(res) == 0:
                return False
            num = happy_sm.index(i)
            sad_num = sad_sm[num]
            if res[-1] == sad_num:
                res = res[:-1]
            else:
                return False
    if len(res) == 0:
        return True
    else:
        return False
