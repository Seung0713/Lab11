def bin(decimal):
    if decimal == 0:
        return ''
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def capitalize(input_string):
    words = input_string.split()
    result = []

    for word in words:
        if word[0].lower() in 'ounds':
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return ' '.join(result)

def partition(input_list, partition_size):
    result = []
    for i in range(0, len(input_list), partition_size):
        sublist = input_list[i:i + partition_size]
        result.append(sublist)
    if len(result[-1]) != partition_size:  # Check if the last sublist is not full
        result.append([])  # Append an empty list if the last one is not full
    return result