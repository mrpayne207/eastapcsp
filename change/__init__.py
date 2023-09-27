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
    output = "1 Qquarter(s)\n1 dime(s)\n1 nickle(s)\n1 pennie(s)"
    check50.run("python3 change.py").stdin(input1, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test93():
    """input of .93 has correct results"""
    input1 = ".93"
    output = "3 quarter(s)\n1 dime(s)\n1 nickle(s)\n3 pennie(s)"
    check50.run("python3 change.py").stdin(input1, prompt=True).stdout(regex(output), output, regex=True).exit()

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
