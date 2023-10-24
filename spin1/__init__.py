import check50
from re import escape


@check50.check()
def exists():
    """spin1.py exists"""
    check50.exists("spin.py")
