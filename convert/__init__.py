import check50
from re import escape


@check50.check()
def exists():
    """convert.py exists"""
    check50.exists("convert.py")

@check50.check(exists)
def test_100():
    """input of 100 yields correct results"""
    input1 = "100"
    output = "37.78"
    check50.run("python3 convert.py").stdin(input1, prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
