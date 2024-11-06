import check50
from re import escape


@check50.check()
def exists():
    """exchange.py exists"""
    check50.exists("exchange.py")

@check50.check(exists)
def test_MXN():
    """input of 78 USD to MXN at 17.08 rate is 1,332.24"""
    input1 = "78"
    input2 = "MXN"
    input3 = "17.08"
    output = "78.00 USD is worth 1,332.24 MXN"
    check50.run("python3 exchange.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_PLN():
    """input of 531 USD to PLN at 4.36 rate is 2,315.16"""
    input1 = "531"
    input2 = "PLN"
    input3 = "4.36"
    output = "531.00 USD is worth 2,315.16 PLN"
    check50.run("python3 exchange.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdout(regex(output), output, regex=True).exit()

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
