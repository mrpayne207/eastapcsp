import check50
from re import escape


@check50.check()
def exists():
    """rps1.py exists"""
    check50.exists("rps1.py")


@check50.check(exists)
def test_p2wins():
    """input of \"R\" and \"P\" results in \"PLAYER 2 WINS\""""
    input = ["R", "P"]
    output = "PLAYER 2 WINS"
    check50.run("python3 rps1.py").stdin(input[0], prompt=True).stdin(input[1], prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_p1wins():
    """input of \"s\" and \"p\" results in \"PLAYER 1 WINS\""""
    input = ["s", "p"]
    output = "PLAYER 1 WINS"
    check50.run("python3 rps1.py").stdin(input[0], prompt=True).stdin(input[1], prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_tie():
    """input of \"p\" and \"p\" results in \"TIE\""""
    input = ["p", "p"]
    output = "TIE"
    check50.run("python3 rps1.py").stdin(input[0], prompt=True).stdin(input[1], prompt=True).stdout(regex(output), output, regex=True).exit()
    
@check50.check(exists)
def test_invalid():
    """input of \"f\" and \"b\" results in \"Make sure to enter r for rock, p for paper and s for scissors\""""
    input = ["f", "b"]
    output = "Make sure to enter r for rock, p for paper and s for scissors"
    check50.run("python3 rps1.py").stdin(input[0], prompt=True).stdin(input[1], prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def main_function():
    """main function exists"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py main_function").exit(0)

@check50.check(exists)
def custom_function():
    """implemented at least 2 top-level function other than main"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py custom_functions").exit(0)

def regex(play):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(play)}\s*$'
