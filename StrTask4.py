import re

string = "dfgh     sdfgdfg dfgfgdf    dfgdfg"
a = re.sub(r'\s+', ' ', string)
print(a)