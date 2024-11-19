
def calculator():
    print("Options:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    while True:
        choice = input("Choose an operation: ")
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == "1":
                print(f"Result: {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1 * num2}")
            elif choice == "4":
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero!")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

calculator()
