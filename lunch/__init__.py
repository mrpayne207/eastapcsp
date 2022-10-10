import check50
from re import escape


@check50.check()
def exists():
    """lunch.py exists"""
    check50.exists("lunch.py")


@check50.check(exists)
def test_alunch():
    """input of 11:44 yields output of \"A Lunch\""""
    input = "11:26"
    output = "A Lunch"
    check50.run("python3 lunch.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_alunch2():
    """input of 12:06 yields output of \"A Lunch\""""
    input = "12:06"
    output = "A Lunch"
    check50.run("python3 lunch.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_blunch():
    """input of 12:07 yields output of \"B Lunch\""""
    input = "12:07"
    output = "B Lunch"
    check50.run("python3 lunch.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_blunch2():
    """input of 12:46 yields output of \"B Lunch\""""
    input = "12:46"
    output = "B Lunch"
    check50.run("python3 lunch.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_clunch():
    """input of 12:47 yields output of \"C Lunch\""""
    input = "12:47"
    output = "C Lunch"
    check50.run("python3 lunch.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()
    
@check50.check(exists)
def test_clunch2():
    """input of 13:26 yields output of \"C Lunch\""""
    input = "13:26"
    output = "C Lunch"
    check50.run("python3 lunch.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_no_output():
    """input of 11:00 yields output of \"No lunch at this time\""""
    input = "11:00"
    output = "No lunch at this time"
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(time):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(time)}\s*$'
