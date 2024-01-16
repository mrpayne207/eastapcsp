import check50
from re import escape


@check50.check()
def exists():
    """grade.py exists"""
    check50.exists("grade.py")

@check50.check(exists)
def testLetter():
    """grade.py rejects letter input"""
    check50.run("python3 grade.py").stdin("a", prompt=True).reject()

@check50.check(exists)
def testSymbol():
    """grade.py rejects non-integer input"""
    check50.run("python3 grade.py").stdin("!", prompt=True).reject()
    
@check50.check(exists)
def testFloat():
    """grade.py rejects float input for number of grades"""
    check50.run("python3 grade.py").stdin("0.1", prompt=True).reject()
    
@check50.check(exists)
def testGrade():
    """grade.py rejects grade out of bounds between 0 and 100"""
    input1 = "1"
    input2 = "-1"
    input3 = "101"
    check50.run("python3 grade.py").stdin(input1, prompt=True).stdin(input2, prompt=True).reject()

@check50.check(exists)
def testA():
    """grades of [85, 90, 95] result in 90.0 and an A"""
    input1 = "3"
    input2 = "85"
    input3 = "90"
    input4 = "95"
    output = "Minimum Grade: 85\nMaximum Grade: 95\nAverage Grade: 90.0, Letter Grade: A"
    check50.run("python3 grade.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def testB():
    """grades of [88, 89, 91] result in 89.3 and an B"""
    input1 = "3"
    input2 = "88"
    input3 = "89"
    input4 = "91"
    output = "Minimum Grade: 88\nMaximum Grade: 91\nAverage Grade: 89.3, Letter Grade: B"
    check50.run("python3 grade.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def testC():
    """grades of [70, 75] result in 72.5 and an C"""
    input1 = "2"
    input2 = "70"
    input3 = "75"
    output = "Minimum Grade: 70\nMaximum Grade: 75\nAverage Grade: 72.5, Letter Grade: C"
    check50.run("python3 grade.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def testD():
    """grades of [68, 69, 72] result in 69.7 and an D"""
    input1 = "3"
    input2 = "68"
    input3 = "69"
    input4 = "72"
    output = "Minimum Grade: 68\nMaximum Grade: 72\nAverage Grade: 69.7, Letter Grade: D"
    check50.run("python3 grade.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def testF():
    """grades of [0, 50, 100] result in 50.0 and an F"""
    input1 = "3"
    input2 = "40"
    input3 = "50"
    input4 = "60"
    output = "Minimum Grade: 40\nMaximum Grade: 60\nAverage = 50.0, Letter Grade = F"
    check50.run("python3 grade.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdin(input3, prompt=True).stdin(input4, prompt=True).stdout(regex(output), output, regex=True).exit()

    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
