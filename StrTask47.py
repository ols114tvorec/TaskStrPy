import re

def task47(line):
    s = re.sub(r'abc\d', '', line)
    print(s)
   