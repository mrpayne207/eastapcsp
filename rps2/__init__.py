import check50
from re import escape


@check50.check()
def exists():
    """rps2.py exists"""
    check50.exists("rps2.py")


@check50.check(exists)
def test_p1isR():
    """input of \"R\" for Player 1 matches \"TIE\" for \"Computer = r\", \"COMPUTER WINS\" for \"Computer = p\" or \"PLAYER 1 WINS\" for \"Computer = s\""""
    output = check50.run("python3 rps2.py").stdin("R").stdout()
    if not any(answer in output for answer in ["Computer = r, TIE", "Computer = p, COMPUTER WINS", "Computer = s, PLAYER 1 WINS"]):
      raise check50.Failure("no match found")
