def exam (n):
    n = str(n)
    examination0 = 0
    while examination0 < 1:
        if n.isdigit() == 1:
            n = int(n)
            examination0 += 1
        else:
            n = str(input('Повторите ввод: '))
    return n
