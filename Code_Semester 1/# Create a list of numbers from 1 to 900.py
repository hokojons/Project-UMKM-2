# Create a list of numbers from 1 to 900
numbers_list = list(range(1, 901))

# Function to search and return the list of numbers
def search_numbers(numbers, search_value):
    if search_value in numbers:
        return f"{search_value} is in the list."
    else:
        return f"{search_value} is not in the list."

# Example usage
search_value = 901
message = search_numbers(numbers_list, search_value)

# Print the message
print(message)

