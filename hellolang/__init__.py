import check50

@check50.check()
def exists():
    """hellolang.py exists."""
    check50.exists("hellolang.py")

@check50.check(exists)
def veronica():
    """responds to name Emma."""
    check50.run("python3 hellolang.py").stdin("Emma").stdout("Emma").exit()

@check50.check(exists)
def brian():
    """responds to name Rodrigo."""
    check50.run("python3 hellolang.py").stdin("Rodrigo").stdout("Rodrigo").exit()
