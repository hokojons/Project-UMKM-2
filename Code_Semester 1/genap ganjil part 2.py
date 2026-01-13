def check_genap_ganjil(n):
    return "genap" if n % 2 == 0 else "ganjil"

while True:
    # Get user input
    try:
        number = int(input("Enter a number (or type 'exit' to quit): "))
        
        genap_numbers = []
        ganjil_numbers = []
        
        for i in range(number + 1):
            if check_genap_ganjil(i) == "genap":
                genap_numbers.append(i)
            else:
                ganjil_numbers.append(i)
        
        # Show genap numbers if they exist
        if genap_numbers:
          print("Genap numbers:", genap_numbers)
        
        # Show ganjil numbers if they exist
        if ganjil_numbers:
           print("Genap numbers:", ganjil_numbers)
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nExiting the program.")
        break