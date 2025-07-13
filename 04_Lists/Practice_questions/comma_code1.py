def format_list(items):
    if not items:
        return "The list is empty."
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ' and ' + items[-1]

user_input = input("Enter items separated by spaces: ")
items_list = user_input.split()  # Splits into a list

print(format_list(items_list))