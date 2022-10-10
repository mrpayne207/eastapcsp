import check50


@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name Veronica."""
    check50.run("python3 hello.py").stdin("Veronica", prompt=True).stdout("hello, Veronica").exit()

@check50.check(exists)
def david():
    """responds to name David"""
    check50.run("python3 hello.py").stdin("David", prompt=True).stdout("hello, David").exit()
