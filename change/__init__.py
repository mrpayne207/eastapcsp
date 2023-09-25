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

@check50.check(exists)
def main_function():
    """main function exists"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py main_function").exit(0)


@check50.check(exists)
def custom_function():
    """implemented at least 1 top-level function other than main"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py custom_functions").exit(0)

def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
