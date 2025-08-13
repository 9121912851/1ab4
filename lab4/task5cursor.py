def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print("Error: File does not exist.")
        return -1

if __name__ == "__main__":
    user_file = input("Enter the path to the text file: ")
    line_count = count_lines_in_file(user_file)
    print("Number of lines:", line_count)
