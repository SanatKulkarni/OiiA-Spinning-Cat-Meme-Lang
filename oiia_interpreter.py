import re
import webbrowser

class OiiaInterpreter:
    def __init__(self):
        self.variables = {}  # Stores variables
        self.arithmetic_stack = []  # Stack for arithmetic operations
        self.control_flow_stack = []  # Stack for if-else conditions
        self.loop_stack = []  # Stack for while loop conditions
        self.functions = {}  # Stores user-defined functions

    def tokenize(self, line):
        # Tokenize the line into "oiia", "true", "false", and numerical values
        pattern = r'oiia+|true|false|\d+'
        tokens = re.findall(pattern, line)
        return tokens

    def interpret(self, code):
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            i = self.execute_line(line, lines, i)

    def execute_line(self, line, lines, line_index):
        try:
            tokens = self.tokenize(line)
            oiia_count = tokens.count('oiia')
            values = [token for token in tokens if token not in {'oiia', 'true', 'false'}]
            bools = [token for token in tokens if token in {'true', 'false'}]
            
            # Handle numerical values
            for token in tokens:
                if token.isdigit():
                    self.arithmetic_stack.append(int(token))
            
            # Handle boolean values for conditions
            if bools:
                if oiia_count == 12:
                    condition = bools[0].lower() == 'true'
                    self.control_flow_stack.append(condition)
                elif oiia_count == 9:
                    condition = bools[0].lower() == 'true'
                    self.loop_stack.append(condition)
            
            # Proceed with command based on oiia_count
            if oiia_count == 4:
                # Variable declaration and assignment
                if not self.arithmetic_stack:
                    raise ValueError("No value on stack to assign to variable.")
                var_name = f"var_{len(self.variables) + 1}"
                value = self.arithmetic_stack.pop()
                self.variables[var_name] = value
                print(f"Declared and assigned variable: {var_name} = {value}")
            elif oiia_count == 5:
                # Addition
                if len(self.arithmetic_stack) >= 2:
                    a = self.arithmetic_stack.pop()
                    b = self.arithmetic_stack.pop()
                    result = a + b
                    self.arithmetic_stack.append(result)
                    print(f"Added {a} and {b}: {result}")
                else:
                    raise ValueError("Not enough values in stack for addition.")
            elif oiia_count == 6:
                # Subtraction
                if len(self.arithmetic_stack) >= 2:
                    a = self.arithmetic_stack.pop()
                    b = self.arithmetic_stack.pop()
                    result = b - a  # Ensure correct order
                    self.arithmetic_stack.append(result)
                    print(f"Subtracted {a} from {b}: {result}")
                else:
                    raise ValueError("Not enough values in stack for subtraction.")
            elif oiia_count == 7:
                # Multiplication
                if len(self.arithmetic_stack) >= 2:
                    a = self.arithmetic_stack.pop()
                    b = self.arithmetic_stack.pop()
                    result = a * b
                    self.arithmetic_stack.append(result)
                    print(f"Multiplied {a} and {b}: {result}")
                else:
                    raise ValueError("Not enough values in stack for multiplication.")
            elif oiia_count == 8:
                # Division
                if len(self.arithmetic_stack) >= 2:
                    a = self.arithmetic_stack.pop()
                    b = self.arithmetic_stack.pop()
                    if a == 0:
                        raise ValueError("Division by zero is not allowed.")
                    result = b / a  # Ensure correct order
                    self.arithmetic_stack.append(result)
                    print(f"Divided {b} by {a}: {result}")
                else:
                    raise ValueError("Not enough values in stack for division.")
            elif oiia_count == 12:
                # Conditional statement (if-else)
                if bools:
                    condition = bools[0].lower() == 'true'
                else:
                    condition = False
                self.control_flow_stack.append(condition)
                if condition:
                    print("Condition is true: Executing if block")
                    # Execute the next block of code (indented lines)
                    i += 1
                    while i < len(lines) and lines[i].startswith("    "):
                        i = self.execute_line(lines[i].strip(), lines, i)
                else:
                    print("Condition is false: Executing else block")
                    # Execute the else block (indented lines)
                    i += 1
                    while i < len(lines) and lines[i].startswith("    "):
                        i = self.execute_line(lines[i].strip(), lines, i)
                return i
            elif oiia_count == 9:
                # While loop
                if len(self.loop_stack) >= 1:
                    condition = self.loop_stack.pop()
                    if condition:
                        print("While loop: Condition is true, repeating code block")
                        # Execute the loop body (indented lines)
                        loop_start = i + 1
                        while loop_start < len(lines) and lines[loop_start].startswith("    "):
                            loop_start = self.execute_line(lines[loop_start].strip(), lines, loop_start)
                        # Re-evaluate the condition
                        self.loop_stack.append(condition)
                    else:
                        print("While loop: Condition is false, exiting loop")
                else:
                    raise ValueError("No condition found for while loop.")
            elif oiia_count == 3:
                # Output command to play Oiia Cat video
                video_url = "https://www.youtube.com/watch?v=C43p8h99Cs0"
                webbrowser.open(video_url)
                print("Output: Oiia Cat video played!")
            else:
                raise ValueError(f"Unknown command: {line}")
        except Exception as e:
            print(f"Error: {e}")
        return line_index + 1