#2- Write a Python program to read first n lines of a file
n = 100
filename = 'C:/Users/Fatoom/Documents/text_files/numbers2.txt'
size = 0
try:
    with(open(filename, 'r')) as f:

        lines = [next(f).strip() for _ in range(n)]

        # Print the lines
        print(f"First {n} lines of the file:")
        for line in lines:
            print(line)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except StopIteration:
    print(f"The file '{filename}' has fewer than {n} lines.")