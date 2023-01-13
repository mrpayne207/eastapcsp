import check50
from re import escape


@check50.check()
def exists():
    """selection_sort.py exists"""
    check50.exists("selection_sort.py")

@check50.check(exists)
def testNumber():
    """selection_sort.py rejects letter input"""
    check50.run("python3 selection_sort.py").stdin("a", prompt=True).reject()

@check50.check(exists)
def testSymbol():
    """selection_sort.py rejects non-integer input"""
    check50.run("python3 selection_sort.py").stdin("!", prompt=True).reject()
    
@check50.check(exists)
def testFloat():
    """selection_sort.py rejects float input"""
    check50.run("python3 selection_sort.py").stdin("0.1", prompt=True).reject()

@check50.check(exists)
def test_list():
    """input of [1, 3, 8, 0, -5, -1] sorts correction"""
    input1 = 6
    input2 = 1
    input3 = 3
    input4 = 8
    input5 = 0
    input6 = -5
    input7 = -1
    output = "Round 0: [1, 3, 8, 0, -5, -1]\nRound 1: [-5, 3, 8, 0, 1, -1]\nRound 2: [-5, -1, 8, 0, 1, 3]\nRound 3: [-5, -1, 0, 8, 1, 3]\nRound 4: [-5, -1, 0, 1, 8, 3]\nRound 5: [-5, -1, 0, 1, 3, 8]"
    check50.run("python3 selection_sort.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdin(input5, prompt=True).stdin(input6, prompt=True).stdin(input7, prompt=True).stdout(regex(output), output, regex=True).exit()

  
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
