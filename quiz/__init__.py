import check50
from re import escape


@check50.check()
def exists():
    """bquiz.py exists"""
    check50.exists("quiz.py")

@check50.check(exists)
def testNumber():
    """quiz.py rejects letter input"""
    check50.run("python3 quiz.py").stdin("a", prompt=True).reject()

@check50.check(exists)
def testSymbol():
    """quiz.py rejects non-integer input"""
    check50.run("python3 quiz.py").stdin("!", prompt=True).reject()
    
@check50.check(exists)
def testFloat():
    """quiz.py rejects float input"""
    check50.run("python3 quiz.py").stdin("0.1", prompt=True).reject()
  
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
