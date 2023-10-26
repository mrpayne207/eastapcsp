import sys
from inspect import getmembers, isfunction

match sys.argv[1]:

    case "main_function":
        with open("create2.py") as file:

            # Look for main function definition and avoid importing any libraries
            assert "def main" in "".join(file.read().splitlines())

    case "custom_functions":
        with open("create2.py") as file:
            function_counter = 0
            condition_counter = 0
            loop_counter = 0
            for line in file.readlines():
                if "def main" in line.strip():
                    continue
                elif "def" in line.strip():
                    function_counter += 1
                if ("if" or "elif" or "else") in line.strip():
                    condition_counter += 1
                  
            
            # Ensure there are at least 1 top-level functions other than main
            assert function_counter >= 1
            
            # Ensure there are at least 1 top-level functions other than main
            assert condition_counter >= 1
    
    case "condition":
        with open("create3.py") as file:
            condition_counter = 0
            for line in file.readlines():
                if "def main" in line.strip():
                    continue
                elif "def" in line.strip():
                    continue
                if ("if" or "elif" or "else") in line.strip():
                    condition_counter += 1
            
            # Ensure there are at least 1 top-level functions other than main
            assert condition_counter >= 1
            
