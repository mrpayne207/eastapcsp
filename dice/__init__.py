import check50
from re import escape


@check50.check()
def exists():
    """dice.py exists"""
    check50.exists("dice.py")

@check50.check(exists)
def test_string_level():
    """dice.py rejects non-numeric dice"""
    check50.run("python3 dice.py").stdin("cat", prompt=True).reject()

@check50.check(exists)
def test_integer_level():
    """dice.py rejects decimal dice"""
    check50.run("python3 dice.py").stdin("0.1", prompt=True).reject()
    
    @check50.check(exists)
def test_integer_level():
    """dice.py rejects out-of-range dice"""
    check50.run("python3 dice.py").stdin("0", prompt=True).reject()
    
@check50.check(exists)
def test_valid_level():
    """dice.py accepts valid dice"""
    check50.run("python3 dice.py").stdin("2", prompt=True).kill()
