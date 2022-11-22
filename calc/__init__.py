import check50


@check50.check()
def exists():
    """calc.py exists"""
    check50.exists("calc.py")

@check50.check(exists)
def test():
    """input of x = 4.32 and y = 8.67 yields correct results"""
    check50.run("python3 calc.py").stdin("4.32", prompt=True).stdin("8.67", prompt=True).stdout('x + y = 12.99').exit()
