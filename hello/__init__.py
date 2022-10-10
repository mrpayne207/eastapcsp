import check50


@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name Veronica."""
    check50.run("python3 hello.py").stdin("Veronica", prompt=False).stdout("hello, Veronica").exit()

@check50.check(exists)
def david():
    """responds to name David"""
    check50.run("python3 hello.py").stdin("David", prompt=False).stdout("hello, David").exit()
