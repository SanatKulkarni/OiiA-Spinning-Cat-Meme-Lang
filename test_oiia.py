from oiia_interpreter import OiiaInterpreter

# Create an instance of the OiiaInterpreter
interpreter = OiiaInterpreter()

# Test code with variables, arithmetic, control flow, and looping
test_code = """
oiia oiia oiia oiia 10  # Declare var_1 and assign 10
oiia oiia oiia oiia 5   # Declare var_2 and assign 5
oiia oiia oiia oiia oiia  # Add var_1 and var_2
oiia oiia oiia oiia oiia oiia  # Subtract var_2 from var_1
oiia oiia oiia oiia oiia oiia oiia  # Multiply var_1 and var_2
oiia oiia oiia oiia oiia oiia oiia oiia  # Divide var_1 by var_2

oiia oiia oiia oiia oiia oiia oiia oiia oiia oiia oiia oiia true  # If-else example
    oiia oiia oiia  # Output (if block)
    oiia oiia oiia  # Output (if block)
oiia oiia oiia oiia oiia oiia oiia oiia oiia oiia oiia oiia false  # Else block
    oiia oiia oiia  # Output (else block)

oiia oiia oiia oiia oiia oiia true  # While loop example
    oiia oiia oiia  # Output (loop body)
    oiia oiia oiia  # Output (loop body)

oiia oiia oiia  # Play Oiia Cat video
"""

# Run the test code
interpreter.interpret(test_code)