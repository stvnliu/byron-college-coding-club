# The Fibonacci sequence is a series of numbers that, when given 2 initial values,
# each value after is given by the sum of the value before and the value 2 places behind.

# For example, a fibonacci sequence of length 8 can be: 1, 1, 2, 3, 5, 8, 13, 21, 
length = 0
seq = []

seq.append(int(input("Input the first number of the sequence: ")))
seq.append(int(input("Input the second number of the sequence: ")))
length = int(input("How long will this sequence be?: "))
if length > 0:
    for i in range(length):
        nextNum = seq[i]+seq[i+1]
        seq.append(nextNum)
    print(seq)
else:
    print("The length can only be positive!")