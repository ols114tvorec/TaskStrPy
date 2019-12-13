def task13(a):
    res1 = 0
    for c in a:
        if c == "+" or c == "-":
            res1 = res1 + 1
    print('Cимволов "+" и "-": ', res1)
    print('Кол-во символов "+" и "-" после которых цифра 0: ', a.count('+0') + a.count('-0'))