import check50


@check50.check()
def exists():
    """lowercase.py exists"""
    check50.exists("lowercase.py")

@check50.check(exists)
def testhello():
    """input of HELLO yields output of hello"""
    check50.run("python3 lowercase.py").stdin("HELLO", prompt=False).stdout("hello").exit()

@check50.check(exists)
def testcs50():
    """input of THIS IS CS50 yields output of this is cs50"""
    check50.run("python3 lowercase.py").stdin("THIS IS CS50", prompt=False).stdout("this is cs50").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("python3 lowercase.py").stdin("50", prompt=False).stdout("50").exit()
