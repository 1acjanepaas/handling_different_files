def find_highest_gwa():
    # Get filename from user
    filename = input("Enter the name of the input file: ")
    
    try:
        # Open and read the file
        with open("student_gwa.txt", "r") as file:
            max_gwa = -1
            max_student = ""
            
            # Read each line from the file
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # Split line into name and GWA (assuming format: "Name GWA")
                parts = line.split()
                if len(parts) < 2:
                    print(f"Warning: Invalid format on line {line_num}: {line}")
                    continue
                
                try:
                    # Extract name (all parts except the last one) and GWA (last part)
                    student_name = ' '.join(parts[:-1])
                    gwa = float(parts[-1])
                    
                    # Check if this GWA is higher than the current maximum
                    if gwa > max_gwa:
                        max_gwa = gwa
                        max_student = student_name
                    
                except ValueError:
                    print(f"Warning: Invalid GWA on line {line_num}: {line}")
                    continue
            
            # Output the result
            if max_student:
                print(f"\nStudent with highest GWA:")
                print(f"Name: {max_student}")
                print(f"GWA: {max_gwa:.2f}")
            else:
                print("No valid student data found in the file.")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    find_highest_gwa()