def task39(x, y):
    str1 = x.split()
    str2 = y.split()
    for i in str1:
        print('Кол-во вхождений слова', i, str2.count(i))