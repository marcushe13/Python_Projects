print("--- Simple Calculator ---")

while (True):

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")
    print("5. Exit")

    try:
        operation_1 = int(input("Choose your Operation (5 to exit): "))
    except ValueError:
        print()
        print("!! -- Please enter a number 1-5 -- !!")
        print()
        continue

    if operation_1 == 5:
        print("Thank you for using my calculator! Come again!")
        break

    if operation_1 < 1 or operation_1 > 5:
        print()
        print("!! -- Invalid option. Please choose a number 1-5 -- !!")
        print()
        continue

    try:
        num_1 = float(input("Enter number 1: "))
        num_2 = float(input("Enter number 2: "))
    except ValueError:
        print()
        print("!! -- Invalid Option. Enter a number -- !!")
        print()
        continue

    if operation_1 == 1:
        sum = round(num_1 + num_2, 2)
        print()
        print(f"-- Sum: {sum} --")
    
    elif operation_1 == 2:
        difference = round(num_1 - num_2, 2) 
        print()
        print(f"-- Difference: {difference} --")

    elif operation_1 == 3:
        product = round(num_1 * num_2 , 2)
        print()
        print(f"-- Product: {product} --")
        
    elif operation_1 == 4:
        if num_2 == 0:
            print()
            print("!! -- ERROR: CANNOT DIVIDE BY ZERO -- !!")
            print()
            continue
        quotient = round(num_1 / num_2, 2)
        print()
        print(f"-- Quotient: {quotient} --")

    print()
    print("New Operation?")







