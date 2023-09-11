import check50
from re import escape


@check50.check()
def exists():
    """hello_world.py exists"""
    check50.exists("hello_world.py")

@check50.check(exists)
def test():
    """running python hello_world.py produces correct output"""
    output = "hello, world!"
    check50.run("python3 hello_world.py").stdout(regex(output), output, regex=True).exit()
    
def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
