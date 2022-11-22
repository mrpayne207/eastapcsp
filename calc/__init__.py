import check50


@check50.check()
def exists():
    """calc.py exists"""
    check50.exists("calc.py")

@check50.check(exists)
def test():
    """input of x = 4.32 and y = 8.67 yields correct results"""
    input1 = "4.32"
    input2 = "8.67"
    output = "x + y = 12.99"
    check50.run("python3 calc.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
