def format_name(first, last):
    return f"{last},{first}"

# Take input from the user for three names and print them formatted
for i in range(3):
    first = input(f"Enter first name for person {i+1}: ")
    last = input(f"Enter last name for person {i+1}: ")
    print(format_name(first, last))


