import check50
from re import escape


@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name Veronica."""
    input = "Veronica"
    output = "hello, Veronica"
    check50.run("python3 hello.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def david():
    """responds to name David"""
    input = "David"
    output = "hello, David"
    check50.run("python3 hello.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()
