import check50
from re import escape


@check50.check()
def exists():
    """word_checker.py exists"""
    check50.exists("word_checker.py")

@check50.check(exists)
def testNumber():
    """word_checker.py rejects numeric word input"""
    check50.run("python3 word_checker.py").stdin("1", prompt=True).reject()

@check50.check(exists)
def testSymbol():
    """word_checker.py rejects non-letter word input"""
    check50.run("python3 word_checker.py").stdin("hello!", prompt=True).reject()
    
@check50.check(exists)
def testShort():
    """word_checker.py rejects short word input"""
    check50.run("python3 word_checker.py").stdin("no", prompt=True).reject()

@check50.check(exists)
def testLong():
    """word_checker.py rejects long word input"""
    check50.run("python3 word_checker.py").stdin("toolong", prompt=True).reject()
    
@check50.check(exists)
def testNumGuess():
    """word_checker.py rejects number guess input"""
    check50.run("python3 word_checker.py").stdin("hello", prompt=True).stdin("greeting", prompt=True).stdin("1", prompt=True).reject()

@check50.check(exists)
def testSymbolGuess():
    """word_checker.py rejects non-letter guess input"""
    check50.run("python3 word_checker.py").stdin("hello", prompt=True).stdin("greeting", prompt=True).stdin("$", prompt=True).reject()

@check50.check(exists)
def testDoubleGuess():
    """word_checker.py rejects non-single letter guess input"""
    check50.run("python3 word_checker.py").stdin("hello", prompt=True).stdin("greeting", prompt=True).stdin("ab", prompt=True).reject()

@check50.check(exists)
def test_hello():
    """input of \'hello\' and \'H\', \'E\', \'L\', \'O\' yields correct results"""
    input1 = "hello"
    input2 = "greeting"
    input3 = "H"
    input4 = "E"
    input5 = "L"
    input6 = "O"
    output = "EXCELLENT, the word was HELLO\nYOU WIN!!!"
    check50.run("python3 word_checker.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdin(input5, prompt=True).stdin(input6, prompt=True).stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
