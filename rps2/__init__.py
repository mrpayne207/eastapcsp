import check50
from re import escape


@check50.check()
def exists():
    """rps2.py exists"""
    check50.exists("rps2.py")


@check50.check(exists)
def test_p1isROCK():
    """input of \"R\" for Player 1 matches \"TIE\" for \"Computer = r\", \"COMPUTER WINS\" for \"Computer = p\" or \"PLAYER 1 WINS\" for \"Computer = s\""""
    output = check50.run("python3 rps2.py").stdin("R", prompt = True).stdout()
    if not any(answer in output for answer in ["Computer: r\nTIE", "Computer: p\nCOMPUTER WINS", "Computer: s\nPLAYER 1 WINS"]):
      raise check50.Failure("no match found")

@check50.check(exists)
def test_p1isPAPER():
    """input of \"p\" for Player 1 matches \"TIE\" for \"Computer = p\", \"COMPUTER WINS\" for \"Computer = s\" or \"PLAYER 1 WINS\" for \"Computer = r\""""
    output = check50.run("python3 rps2.py").stdin("p", prompt = True).stdout()
    if not any(answer in output for answer in ["Computer: p\nTIE", "Computer: s\nCOMPUTER WINS", "Computer: r\nPLAYER 1 WINS"]):
      raise check50.Failure("no match found")  

@check50.check(exists)
def test_p1isSCISSOR():
    """input of \"s\" for Player 1 matches \"TIE\" for \"Computer = s\", \"COMPUTER WINS\" for \"Computer = r\" or \"PLAYER 1 WINS\" for \"Computer = p\""""
    output = check50.run("python3 rps2.py").stdin("s", prompt = True).stdout()
    if not any(answer in output for answer in ["Computer: s\nTIE", "Computer: r\nCOMPUTER WINS", "Computer: p\nPLAYER 1 WINS"]):
      raise check50.Failure("no match found")  

@check50.check(exists)
def test_invalid():
    """input of \"f\" for Player 1 results in \"Make sure to enter r for rock, p for paper or s for scissors\""""
    output = check50.run("python3 rps2.py").stdin("f", prompt = True).stdout()
    if not any(answer in output for answer in ["Make sure to enter r for rock, p for paper or s for scissors"]):
      raise check50.Failure("no match found") 

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
