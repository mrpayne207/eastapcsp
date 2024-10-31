import check50
import re

@check50.check()
def exists():
    """relativity.py exists"""
    check50.exists("relativity.py")

@check50.check(exists)
def test1():
    """input of 1 includes output of 90000000000000000"""
    output = check50.run("python3 relativity.py").stdin("1", prompt=True).stdout("90000000000000000").exit()

@check50.check(exists)
def test14():
    """input of 14 includes output of 1260000000000000000"""
    check50.run("python3 relativity.py").stdin("14", prompt=True).stdout("1260000000000000000").exit()

@check50.check(exists)
def test50():
    """input of 50 includes output of 4500000000000000000"""
    check50.run("python3 relativity.py").stdin("50", prompt=True).stdout("4500000000000000000").exit()
