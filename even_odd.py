number_one = int(input("Please insert a number to verify if it's even or odd: "))
if number_one % 2 == 0:
    print(f"The number {number_one} is even!")
else:
    print(f"The number {number_one} is not even (odd)")


operation = number_one % 2 == 0
print(operation)