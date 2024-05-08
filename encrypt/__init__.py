import check50
from re import escape


@check50.check()
def exists():
    """encrypt.py exists"""
    check50.exists("encrypt.py")


@check50.check(exists)
def test_1_arg():
    """input of \"python encrypt.py\" results in error"""
    output = "Usage: python encrypt.py <key>"
    check50.run("python3 encrypt.py").stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_nonint_arg():
    """input of \"python encrypt.py abcd\" results in error"""
    output = "Usage: python encrypt.py <numeric key>"
    check50.run("python3 encrypt.py a").stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_key1():
    """input of \"python encrypt.py 5182273847\" runs correctly"""
    input = "Free Pizza In The Cafeteria"
    output = "cyphertext: Ksmg Rpche Ps Upg Ehimxlwji"
    check50.run("python3 encrypt.py 5182273847").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_key2():
    """input of \"python encrypt.py 5182273847\" runs correctly"""
    input = "Hello, World!"
    output = "cyphertext: Mftnq, Drzpk!"
    check50.run("python3 encrypt.py 5182273847").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_key3():
    """input of \"python encrypt.py 975318462\" runs correctly"""
    input = "Write the REAL code Nathan!"
    output = "cyphertext: Fynwf blk TNHQ fpli Tccofq!"
    check50.run("python3 encrypt.py 975318462").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

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

def regex(play):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(play)}\s*$'
