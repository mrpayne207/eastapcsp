import check50
from re import escape


@check50.check()
def exists():
    """change.py exists"""
    check50.exists("change.py")

@check50.check(exists)
def test41():
    """input of .41 has correct results"""
    input1 = ".41"
    output = "1 [Qq]uarter(s)\n1 [Dd]ime(s)\n1 [Nn]ickle(s)\n1 [Pp]ennie(s)"
    check50.run("python3 calc.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test93():
    """input of .93 has correct results"""
    input1 = ".93"
    output = "3 [Qq]uarter(s)\n1 [Dd]ime(s)\n1 [Nn]ickle(s)\n3 [Pp]ennie(s)"
    check50.run("python3 calc.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
