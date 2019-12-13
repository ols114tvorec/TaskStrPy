import re

def task4(str):
    a = re.sub(r'\s+', ' ', str)
    print(a)

task4("dfgh     sdfgdfg dfgfgdf    dfgdfg")