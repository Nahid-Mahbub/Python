'''Num_1 = int(input("Give the frist number: "))
Num_2 = int(input("Give the second number: "))
addition = (Num_1 + Num_2)
subtraction = (Num_1 - Num_2)
multiplication = (Num_1 * Num_2)
divition = (Num_1 / Num_2)
print("Addition of number", Num_1," and number", Num_2, "is:", addition)
print("Subtraction of number", Num_1," and number", Num_2, "is:", subtraction)
print("Multiplication of number", Num_1," and number", Num_2, "is:", multiplication)
print("Divition of number", Num_1," and number", Num_2, "is:", divition)
print("The value of a is: ", Num_1)

Advance calculator


while(1):
    Num_1 = int(input("Give the frist number: ")) #Taking the frist number as input
    Num_2 = int(input("Give the second number: ")) #Taking the second number as input
    print("Select operation ")
    print("Addition 1\nSubtraction 2\nMultiplication 3\nDivition 4\nBreak the loop")
    Operation = int(input())
    if(Operation == 1):
        addition = (Num_1 + Num_2)
        print("Addition of number", Num_1," and number", Num_2, "is:", addition)
    elif(Operation == 2):
        subtraction = (Num_1 - Num_2)
        print("Subtraction of number", Num_1," and number", Num_2, "is:", subtraction)
    elif(Operation == 3):
        multiplication = (Num_1 * Num_2)
        print("Multiplication of number", Num_1," and number", Num_2, "is:", multiplication)
    elif(Operation == 4):
        divition = (Num_1 / Num_2)
        print("Divition of number", Num_1," and number", Num_2, "is:", divition)
    else:
        break '''
# Advanced Calculation
Num_1 = int(input("Give the frist number: ")) #Taking the frist number as inpu
Num_2 = int(input("Give the second number: ")) #Taking the second number as input
for i in range(10):
    print(i)
    print("Select operation ")
    print("Update value 0\nAddition 1\nSubtraction 2\nMultiplication 3\nDivition 4\nBreak the loop")
    Operation = int(input())
    if(Operation == 1):
        addition = (Num_1 + Num_2)
        print("Addition of number", Num_1," and number", Num_2, "is:", addition)
    elif(Operation == 2):
        subtraction = (Num_1 - Num_2)
        print("Subtraction of number", Num_1," and number", Num_2, "is:", subtraction)
    elif(Operation == 3):
        multiplication = (Num_1 * Num_2)
        print("Multiplication of number", Num_1," and number", Num_2, "is:", multiplication)
    elif(Operation == 4):
        divition = (Num_1 / Num_2)
        print("Divition of number", Num_1," and number", Num_2, "is:", divition)
    elif(Operation == 0):
        Num_1 = int(input("Give the Update frist number: "))
        Num_2 = int(input("Give the Update second number: "))
    else:
        break

