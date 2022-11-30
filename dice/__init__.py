import check50
from re import escape


@check50.check()
def exists():
    """dice.py exists"""
    check50.exists("dice.py")
