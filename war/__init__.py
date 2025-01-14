import check50
from re import escape


@check50.check()
def exists():
    """create3.py exists"""
    check50.exists("war.py")

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
