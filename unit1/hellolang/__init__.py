import re

from check50 import *

class Hello(Checks):
    
    @check()
    def exists(self):
        """hellolang.py exists."""
        self.require("hellolang.py")
    
    @check("exists")
    def rob(self):
        """responds to name Rob."""
        self.spawn("python hellolang.py").stdin("Rob").stdout("hello, Rob\n")
    
    @check("exists")
    def layla(self):
        """responds to name Layla."""
        self.spawn("python hellolang.py").stdin("Layla").stdout("hello, Layla\n")
