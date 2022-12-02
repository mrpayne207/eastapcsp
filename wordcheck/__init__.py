import check50
from re import escape


@check50.check()
def exists():
    """word_checker.py exists"""
    check50.exists("word_checker.py")

@check50.check(exists)
def test():
    """word_checker.py rejects numeric word input"""
    check50.run("python3 word_checker.py").stdin("1", prompt=True).reject()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
