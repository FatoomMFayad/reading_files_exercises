# Function to read numbers from a file
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip whitespace, and convert to integers
        numbers = {int(line.strip()) for line in file if line.strip().isdigit()}
    return numbers

# File paths
file1 = "C:/Users/Fatoom/Documents/text_files/numbers1.txt"
file2 = "C:/Users/Fatoom/Documents/text_files/numbers2.txt"

# Read numbers from both files
numbers_file1 = read_numbers_from_file(file1)
numbers_file2 = read_numbers_from_file(file2)

# Find overlapping numbers
overlapping_numbers = numbers_file1.intersection(numbers_file2)

# Output the overlapping numbers
print("Overlapping numbers:", overlapping_numbers)
