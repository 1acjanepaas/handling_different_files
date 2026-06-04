class LifeWriter:
    def write_life(self):
      with open("own_life.txt", "w") as file:

        while True:
            line = input("Enter line: ")
            file.write(line + "\n")

            more = input("Are there more lines y/n? ").lower()
            if more != 'y':
                break

    print("Your text has been saved to mylife.txt")