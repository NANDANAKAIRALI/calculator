def multiplication_table(number):
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


try:
    input_number = int(input("Enter a number: "))
    multiplication_table(input_number)
except ValueError:
    print("Please enter a valid number.")

