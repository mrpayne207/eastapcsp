import check50
from re import escape


@check50.check()
def exists():
    """bubble_sort.py exists"""
    check50.exists("bubble_sort.py")

@check50.check(exists)
def testNumber():
    """sbubble_sort.py rejects letter input"""
    check50.run("python3 bubble_sort.py").stdin("a", prompt=True).reject()

@check50.check(exists)
def testSymbol():
    """bubble_sort.py rejects non-integer input"""
    check50.run("python3 bubble_sort.py").stdin("!", prompt=True).reject()
    
@check50.check(exists)
def testFloat():
    """bubble_sort.py rejects float input"""
    check50.run("python3 bubble_sort.py").stdin("0.1", prompt=True).reject()

@check50.check(exists)
def test_list():
    """input of [6, 5, 4, 3, 2, 1] sorts correctly"""
    input1 = "6"
    input2 = "6"
    input3 = "5"
    input4 = "4"
    input5 = "3"
    input6 = "2"
    input7 = "1"
    output = "Round 0: [6, 5, 4, 3, 2, 1]\nRound 1: [5, 4, 3, 2, 1, 6]\nRound 2: [4, 3, 2, 1, 5, 6]\nRound 3: [3, 2, 1, 4, 5, 6]\nRound 4: [2, 1, 3, 4, 5, 6]\nRound 5: [1, 2, 3, 4, 5, 6]"
    check50.run("python3 selection_sort.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdin(input5, prompt=True).stdin(input6, prompt=True).stdin(input7, prompt=True).stdout(regex(output), output, regex=True).exit()

  
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
