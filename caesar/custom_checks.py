import sys
from inspect import getmembers, isfunction

match sys.argv[1]:

    case "main_function":
        with open("caesar.py") as file:

            # Look for main function definition and avoid importing any libraries
            assert "def main" in "".join(file.read().splitlines())

    case "custom_functions":
        with open("caesar.py") as file:
            function_counter = 0
            for line in file.readlines():
                if "def main" in line.strip():
                    continue
                elif "def" in line.strip():
                    function_counter += 1
            
            # Ensure there is at least 1 top-level function other than main
            assert function_counter >= 1
