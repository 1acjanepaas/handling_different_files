import os

class IntegerProcessor:

    def process_file(self):
        try:
            print("SCRIPT RUNNING...")

            # Get the folder where the script is located
            script_folder = os.path.dirname(os.path.abspath(__file__))
            print("SCRIPT FOLDER:", script_folder)
            print("FILES IN SCRIPT FOLDER:", os.listdir(script_folder))

            filename = "integers.txt"
            file_path = os.path.join(script_folder, filename)

            with open(file_path, "r") as file:
                print("FILE OPENED SUCCESSFULLY")

                numbers = []
                for line_num, line in enumerate(file, 1):
                    line = line.strip()

                    if not line:
                        continue

                    try:
                        numbers.append(int(line))
                    except ValueError:
                        print(f"Invalid line {line_num}: {line}")

            print("NUMBERS READ:", numbers)

            even_squares = []
            odd_cubes = []

            for num in numbers:
                if num % 2 == 0:
                    even_squares.append(num ** 2)
                else:
                    odd_cubes.append(num ** 3)

            with open(os.path.join(script_folder, "double.txt"), "w") as f:
                for n in even_squares:
                    f.write(str(n) + "\n")

            with open(os.path.join(script_folder, "triple.txt"), "w") as f:
                for n in odd_cubes:
                    f.write(str(n) + "\n")

            print("DONE!")

        except FileNotFoundError:
            print("ERROR: integers.txt NOT FOUND in this folder.")
        except Exception as e:
            print("ERROR OCCURRED:", e)


if __name__ == "__main__":
    IntegerProcessor().process_file()