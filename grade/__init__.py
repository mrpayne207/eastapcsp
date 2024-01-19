import check50
from re import escape


@check50.check()
def exists():
    """grade1.py exists"""
    check50.exists("grade1.py")

@check50.check(exists)
def testLetter():
    """grade1.py rejects letter input"""
    check50.run("python3 grade1.py").stdin("a", prompt=True).reject()

@check50.check(exists)
def testSymbol():
    """grade1.py rejects non-integer input"""
    check50.run("python3 grade1.py").stdin("!", prompt=True).reject()
    
@check50.check(exists)
def testFloat():
    """grade1.py rejects float input for number of grades"""
    check50.run("python3 grade1.py").stdin("0.1", prompt=True).reject()
    
@check50.check(exists)
def testGrade():
    """grade1.py rejects grade out of bounds between 0 and 100"""
    input1 = "1"
    input2 = "-1"
    input3 = "101"
    check50.run("python3 grade1.py").stdin(input1, prompt=True).stdin(input2, prompt=True).reject()

@check50.check(exists)
def testRetake():
    """grades of [73, 78, 86, 61, 100] produce correct result"""
    input1 = "5"
    input2 = "73"
    input3 = "78"
    input4 = "86"
    input5 = "61"
    input6 = "100"
    output = "Average Grade: 79.6\nYou should retake Test 1, your score was: 73\nYou should retake Test 2, your score was: 78\nYou should retake Test 4, your score was: 613"
    check50.run("python3 grade1.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdin(input5, prompt=True).stdin(input6, prompt=True).stdout(regex(output), output, regex=True).exit()

def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
