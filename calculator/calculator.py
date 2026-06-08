# ====================================
#     SCIENTIFIC CALCULATOR 
# ====================================

import math

welsc = "Scientific Calculator"

print(welsc.center(60, "-"))
print("Type 'exit' to close calculator\n")

while True:

    expression = input("Enter Expression: ")

    if expression == "":
        continue

    if expression.lower() == "exit":
        print("Thanks for using calculator ")
        break

    try:

        # Replace power symbol
        expression = expression.replace("^", "**")

        # Scientific calculation
        result = eval(expression, {"__builtins__": None}, {

            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "factorial": math.factorial,
            "pi": math.pi,
            "e": math.e

        })

        print("Result =", round(result, 4))

    except ZeroDivisionError:
        print("Error! Division by zero.")

    except Exception:
        print("Invalid Expression!")