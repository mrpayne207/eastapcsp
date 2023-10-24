import check50
from re import escape


@check50.check()
def exists():
    """spin.py exists"""
    check50.exists("spin.py")
