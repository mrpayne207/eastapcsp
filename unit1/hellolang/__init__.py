import re

from check50 import *

class Hello(Checks):
    
    @check()
    def exists(self):
        """helloLang.py exists."""
        self.require("helloLang.py")
    
    @check("exists")
    def rob(self):
        """responds to name Rob."""
        self.spawn("python helloLang.py").stdin("Rob").stdout("hello, Rob\n")
    
    @check("exists")
    def layla(self):
        """responds to name Layla."""
        self.spawn("python helloLang.py").stdin("Layla").stdout("hello, Layla\n")
