import check50
from re import escape


@check50.check()
def exists():
    """dice.py exists"""
    check50.exists("dice.py")


@check50.check(exists)
def test_1():
    """input of 1 dice has more than 6 rolls""""
    output = check50.run("python3 dice.py").stdin(1, prompt = True).stdout()
    if int(output) < 6:
      raise check50.Failure("answer not possible")

@check50.check(exists)
def test_2():
    """input of 2 dice has more than 11 rolls""""
    output = check50.run("python3 dice.py").stdin(2, prompt = True).stdout()
    if int(output) < 11:
      raise check50.Failure("answer not possible") 

@check50.check(exists)
def test_3():
    """input of 3 dice has more than 16 rolls""""
    output = check50.run("python3 dice.py").stdin(3, prompt = True).stdout()
    if int(output) < 16:
      raise check50.Failure("answer not possible")  

@check50.check(exists)
def test_4():
    """input of 4 dice has more than 21 rolls""""
    output = check50.run("python3 dice.py").stdin(4, prompt = True).stdout()
    if int(output) < 21:
      raise check50.Failure("answer not possible") 
