import check50
from re import escape


@check50.check()
def exists():
    """calc2.py exists"""
    check50.exists("calc2.py")

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
def test_one_plus_one():
    """input of \"1 + 1\" yields output of 2.0"""
    input = "1 + 1"
    output = "2.0"
    check50.run("python3 calc2.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_two_minus_three():
    """input of \"2 - 3\" yields output of -1.0"""
    input = "2 - 3"
    output = "-1.0"
    check50.run("python3 calc2.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_two_times_two():
    """input of \"2 * 2\" yields output of 4.0"""
    input = "2 * 2"
    output = "4.0"
    check50.run("python3 calc2.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_fifty_divided_by_five():
    """input of \"50 / 5\" yields output of 10.0"""
    input = "50 / 5"
    output = "10.0"
    check50.run("python3 calc2.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_3_divided_by_2():
    """input of \"3 / 2\" yields output of 1.5"""
    input = "3 / 2"
    output = "1.5"
    check50.run("python3 calc2.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(num):
    """match given number with a single floating point decimal; allow only text or whitespace on either side of number"""
    return fr'^[^\d]*{escape(num)}[^\d]*$'
