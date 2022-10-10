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
    items = ["R", "P"]
    output = "PLAYER 2 WINS"
    check50.run("python3 rps1.py").stdin(items[0], prompt=True).stdin(items[1], prompt=True).stdout(regex(output), regex=True).kill()
