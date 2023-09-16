import check50
from re import escape


@check50.check()
def exists():
    """convert.py exists"""
    check50.exists("convert.py")

@check50.check(exists)
def test_100():
    """input of 100 deg F yields 37.8 deg C"""
    input1 = "100"
    output = "37.8"
    check50.run("python3 convert.py").stdin(input1, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_50():
    """input of 50 deg F yields 10.0 deg C"""
    input1 = "50"
    output = "10.0"
    check50.run("python3 convert.py").stdin(input1, prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
