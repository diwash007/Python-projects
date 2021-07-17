logo = """
 _____________________
|  _________________  |
| | Diwash       0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b== 0:
        print("Cannot divide by zero!!")
        return float("inf")
    else:
        return a/b

ops = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide,
}
ch = "no"

while ch != "y":
    num1 = float(input("\nEnter first number: "))

    for key in ops:
        print(key)

    op_symbol = input("Pick a symbol: ")
    num2 = float(input("Enter second number: "))

    if op_symbol  not in ops:
        print("Invalid operator!!")
    else:
        calc_func = ops[op_symbol]
        ans = calc_func(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {ans}\n")

        while 1:
            ch = input(f"Would you like to continue operation with {ans}? 'y' or 'n'?")
            if ch != "y":
                break
            prev_ans = ans
            op_symbol = input("Pick a symbol: ")
            num3 = float(input("Enter another number: "))
            if op_symbol  not in ops:
                print("Invalid operator!!\n")
            else:
                calc_func = ops[op_symbol]
                ans = calc_func(ans,num3)
                print(f"{prev_ans} {op_symbol} {num3} = {ans}\n")

