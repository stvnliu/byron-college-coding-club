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
        print("Your add result is: " + total)
    elif operation == OP_SUB:
        raise NotImplementedError
    elif operation == OP_DIV:
        raise NotImplementedError
    elif operation == OP_MUL:
        raise NotImplementedError
        