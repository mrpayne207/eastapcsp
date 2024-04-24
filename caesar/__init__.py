import check50
from re import escape


@check50.check()
def exists():
    """caesar.py exists"""
    check50.exists("caesar.py")


@check50.check(exists)
def test_1_arg():
    """input of \"python caesar.py\" results in error"""
    output = "Usage: python caesar.py <int>"
    check50.run("python3 rps1.py").stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_nonint_arg():
    """input of \"python caesar.py a\" results in error"""
    output = "Usage: python caesar.py <int>"
    check50.run("python3 caesar.py a").stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_intarg():
    """input of \"python caesar.py 5\" runs correctly"""
    input = "Hello, World!"
    output = "Mjqqt, Btwqi!"
    check50.run("python3 caesar.py 5").stdin(input[0], prompt=True).stdout(regex(output), output, regex=True).exit()

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

def regex(play):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(play)}\s*$'
