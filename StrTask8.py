def task8(line):
    if 'x' in line and 'w' in line:
        if line.index('x') > line.index('w'):
         print('first element - w')
        else:
            print('first element - x')
    else:
        print('Elements is not definted')