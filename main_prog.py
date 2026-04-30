def separate_numbers():
    try:
        # Read numbers from numbers.txt
        with open("number.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]

        # Optional check
        if len(numbers) != 20:
            print(f"Warning: Expected 20 numbers, found {len(numbers)}")

        # Separate even and odd numbers
        even_numbers = []
        odd_numbers = []

        for num in numbers:
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)

        # Write even numbers to even.txt
        with open("even.txt", "w") as even_file:
            for num in even_numbers:
                even_file.write(str(num) + "\n")

        # Write odd numbers to odd.txt
        with open("odd.txt", "w") as odd_file:
            for num in odd_numbers:
                odd_file.write(str(num) + "\n")

        print("Done! Numbers have been separated into even.txt and odd.txt.")

    except FileNotFoundError:
        print("Error: numbers.txt file not found.")
    except ValueError:
        print("Error: Make sure all lines in numbers.txt are integers.")

# Run the function
separate_numbers()