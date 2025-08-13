def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            count = sum(1 for _ in f)
        return count
    except FileNotFoundError:
        print("Error: File not found.")
        return -1

if __name__ == "__main__":
    user_path = input("Enter the path to the text file: ")
    total_lines = count_lines_in_file(user_path)
    print("Total number of lines:", total_lines)