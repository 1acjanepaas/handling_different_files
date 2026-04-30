def process_numbers():
    try:
        # Read numbers from file
        with open("int_number.txt", "r") as file:
            numbers = [int(x) for line in file for x in line.split()]

        # Optional check
        if len(numbers) != 20:
            print(f"Warning: Expected 20 numbers, found {len(numbers)}")

        # Open output files
        with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:

            for num in numbers:
                if num % 2 == 0:
                    # even → square
                    double_file.write(str(num ** 2) + "\n")
                else:
                    # odd → cube
                    triple_file.write(str(num ** 3) + "\n")

        print("Done! Check double.txt and triple.txt.")

    except FileNotFoundError:
        print("Error: integers.txt not found.")
    except ValueError:
        print("Error: Make sure all contents are integers.")

# Run
process_numbers()