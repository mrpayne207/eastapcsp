import check50
from re import escape


@check50.check()
def exists():
    """calc.py exists"""
    check50.exists("calc.py")

@check50.check(exists)
def test():
    """input of x = 4.32 and y = 8.67 yields correct results"""
    input1 = "4.32"
    input2 = "8.67"
    output = "x + y = 12.99\nx - y = -4.35\nx * y = 37.45\nx / y = 0.50\nx mod y = 4.32"
    check50.run("python3 calc.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
