import check50
from re import escape


@check50.check()
def exists():
    """coke.py exists"""
    check50.exists("coke.py")


@check50.check(exists)
def test_25():
    """coke accepts 25 cents"""
    input = "25"
    output = "25"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_10():
    """coke accepts 10 cents"""
    input = "10"
    output = "40"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_5():
    """coke accepts 5 cents"""
    input = "5"
    output = "45"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_invalid():
    """coke rejects invalid amount of cents"""
    input = "30"
    output = "Enter 25 for a quarter, 10 for a dime or 5 for a nickel"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_multiple():
    """coke accepts continued input"""
    input = "10"
    output = "Remaining amount owed: 30 cents"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_terminate():
    """coke terminates at 50 cents"""
    input = "25"
    output = "You paid with the following coins:\nquarter, quarter, \nChange owed back to you: 0 cents"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_change():
    """coke provides correct change"""
    input = "25"
    output = "10"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin("10", prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

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

@check50.check(exists)
def condition():
    """implemented at least 1 condition"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py condition").exit(0)

@check50.check(exists)
def loop():
    """implemented at least 1 loop"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py loop").exit(0)

def regex(text):
    """match case-sensitively, allowing for characters (not numbers) on either side. Ensure not negative with no dashes"""
    return fr'^[^\d-]*{escape(text)}[^\d]*$'
