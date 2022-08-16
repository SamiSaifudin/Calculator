
def user_input():
    while True:
        num_1 = float(input("Enter a number: "))
        op = input("Pick one (+,-, *, /, **, %): ")
        num_2 = float(input("Enter a second number: "))
        if op == "+":
            print(num_1 + num_2)
            break
        elif op == "-":
            print(num_1 - num_2)
            break
        elif op == "*":
            print(num_1 * num_2)
            break
        elif op == "/":
            print(num_1 / num_2)
            break
        elif op == "**":
            print(num_1 ** num_2)
            break
        elif op == "%":
            print(num_1 % num_2)
            break 
        else:
            print("Invalid Operator")
            continue

def replay(): 
    while True:
        Replay = input("Would you like to use the calculator again? Yes or No: ").upper()
        if Replay == "YES":
            user_input()
        elif Replay == "NO":
            break



user_input()
replay()
