def print_backwards(s):
    # Base case: when the string is empty, return
    if s == "":
        return
    # Recursive case: print the last character and call the function on the rest of the string
    print(s[-1], end="")
    print_backwards(s[:-1])

# Test
print_backwards("Hello, world!")

def format_names(names):
    formatted_names = []
    for name in names:
        parts = name.split(", ")
        if len(parts) == 2:
            # Already in "last, first" format
            formatted_names.append(name)
        else:
            first, last = name.split(" ")
            formatted_names.append(f"{last}, {first}")
    return formatted_names

# Test
print(format_names(["Allen Anderson", "Bruce Baker", "Cook, Claire", "Dunn, David"]))

def sum_a(data):
    total = 0
    for item in data:
        total += item.get("a", 0)  # Use get to avoid KeyError if 'a' doesn't exist
    return total

# Test
example_data = [
    {"a": 2, "b": 3, "c": 1},
    {"b": 2, "c": 3},
    {"a": 1, "b": 2, "c": 3},
    {"a": 3, "b": 2, "c": 1},
    {"c": 1, "a": 4},
]
print(sum_a(example_data))

def process_list(numbers):
    even_indexed = [str(numbers[i]) for i in range(0, len(numbers), 2)]
    odd_indexed = [numbers[i] * 10 for i in range(1, len(numbers), 2)]
    return even_indexed + odd_indexed

# Test
print(process_list([0, 1, 2, 3, 4, 5, 6, 7]))
print(process_list([9, 8, 7, 6, 5, 4, 3, 2, 1]))
