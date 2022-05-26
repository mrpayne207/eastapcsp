import check50
import re

@check50.check()
def exists():
    """hellolang.py exists"""
    check50.exists("hellolang.py")

@check50.check(exists)
def compiles():
    """hellolang.py compiles"""
    check50.c.compile("hellolang.py", lcs50=True)
