import os

class GWAFinder:

    def find_highest(self):
        # Get filename from user
        filename = input("Enter the name of the input file: ")

        try:
            # Get the folder where the script is located
            script_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_folder, filename)

            print(f"Looking for file in: {script_folder}")

            # Open and read the file
            with open(file_path, "r") as file:
                max_gwa = -1
                max_student = ""

                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split()
                    if len(parts) < 2:
                        print(f"Warning: Invalid format on line {line_num}: {line}")
                        continue

                    try:
                        student_name = ' '.join(parts[:-1])
                        gwa = float(parts[-1])

                        if gwa > max_gwa:
                            max_gwa = gwa
                            max_student = student_name

                    except ValueError:
                        print(f"Warning: Invalid GWA on line {line_num}: {line}")
                        continue

            if max_student:
                print("\nStudent with highest GWA:")
                print(f"Name: {max_student}")
                print(f"GWA: {max_gwa:.2f}")
            else:
                print("No valid student data found in the file.")

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found in {script_folder}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Run the program
if __name__ == "__main__":
    finder = GWAFinder()
    finder.find_highest()