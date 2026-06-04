import os

class NumberSeparator:

    def separate_numbers(self):
        try:
            # Make sure file is read from the same folder as this script
            filename = os.path.join(os.path.dirname(__file__), "numbers.txt")

            # Read numbers from file
            with open(filename, "r") as file:
                numbers = [int(line.strip()) for line in file if line.strip()]

            # Check if 20 numbers exist
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

            print("Done! Files created: even.txt and odd.txt")

        except FileNotFoundError:
            print("Error: numbers.txt file not found in the same folder as this script.")
        except ValueError:
            print("Error: File must contain only integers, one per line.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")


# Run the program
if __name__ == "__main__":
    processor = NumberSeparator()
    processor.separate_numbers()