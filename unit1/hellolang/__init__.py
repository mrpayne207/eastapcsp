import check50
import check50.c

filename = "hellolang.py"
@check50.check()
def exists():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(exists)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)
