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
    """input of \"p\" and \"p\" results in \"PLAYER 1 WINS\""""
    input = ["p", "p"]
    output = "TIE"
    check50.run("python3 rps1.py").stdin(input[0], prompt=True).stdin(input[1], prompt=True).stdout(regex(output), output, regex=True).exit()
    
@check50.check(exists)
def test_invalid():
    """input of \"f\" and \"b\" results in \"PLAYER 1 WINS\""""
    input = ["f", "b"]
    output = "Make sure to enter r for rock, p for paper or s for scissors"
    check50.run("python3 rps1.py").stdin(input[0], prompt=True).stdin(input[1], prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(play):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(play)}\s*$'
