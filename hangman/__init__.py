import check50
from re import escape


@check50.check()
def exists():
    """hangman.py exists"""
    check50.exists("hangman.py")


@check50.check(exists)
def test_a():
    """accepts a as letter guess"""
    input = "a"
    output = "_ a _ a   a _ _ _ _ a _ _ _ _ _ "
    check50.run("python3 hangman.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_invalid_letter():
    """rejects invalid letter z"""
    input = "z"
    output = "z is NOT in the word, 5 wrong guesses remaining"
    check50.run("python3 hangman.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()

@check50.check(exists)
def test_invalid_character():
    """rejects invalid letter !"""
    input = "!"
    output = "Make sure to enter a single letter."
    check50.run("python3 hangman.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()

@check50.check(exists)
def test_invalid_multiple_characters():
    """rejects invalid letter data"""
    input = "data"
    output = "Make sure to enter a single letter."
    check50.run("python3 hangman.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()

#@check50.check(exists)
#def test_multiple():
#    """coke accepts continued input"""
#    input = "10"
#    output = "Remaining amount owed: 30 cents"
#    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


#@check50.check(exists)
#def test_terminate():
#    """coke terminates at 50 cents"""
#    input = "25"
#    output = "You paid with the following coins:\nquarter, quarter, \nChange owed back to you: 0 cents"
#    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


#@check50.check(exists)
#def test_change():
#    """coke provides correct change"""
#    input = "25"
#    output = "10"
#    check50.run("python3 coke.py").stdin(input, prompt=True).stdin("10", prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def main_function():
    """main function exists"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py main_function").exit(0)


@check50.check(exists)
def custom_function():
    """implemented at least 1 top-level function other than main"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py custom_functions").exit(0)

@check50.check(exists)
def condition():
    """implemented at least 1 condition"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py condition").exit(0)

@check50.check(exists)
def loop():
    """implemented at least 1 loop"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py loop").exit(0)

def regex(text):
    """match case-sensitively, allowing for characters (not numbers) on either side. Ensure not negative with no dashes"""
    return fr'^[^\d-]*{escape(text)}[^\d]*$'
