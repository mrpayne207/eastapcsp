import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """rps1.py exists"""
    check50.exists("rps1.py")

@check50.check(exists)
def test_p2win():
    """input of \"R\", \"P\", results in PLAYER 2 WINS"""
    input1 = "r"
    input2 = "p"
    output = "PLAYER 2 WINS"
    check50.run("python3 rps1.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).exit()
