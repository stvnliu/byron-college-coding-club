OP_ADD = 0
OP_SUB = 1
OP_DIV = 2
OP_MUL = 3
def program(operation: int):
    if operation == OP_ADD:
        total = 0
        acceptMoreInputs = True
        while acceptMoreInputs:
            num = input("Input number (input \"X\" to stop): ")
            if (num == "X"):
                acceptMoreInputs = False
                continue
            total += int(num) # total = total + num
        print("Your add result is: " + str(total))
    elif operation == OP_SUB:
        firstNum: float = float(input("First number: "))
        secondNum: float = float(input("Second number: "))
        return firstNum - secondNum
    elif operation == OP_DIV:
        firstNum: float = float(input("First number: "))
        secondNum: float = float(input("Second number: "))
        return firstNum / secondNum
    elif operation == OP_MUL:
        firstNum: float = float(input("First number: "))
        secondNum: float = float(input("Second number: "))
        return firstNum * secondNum
    else:
        return
program(OP_ADD)