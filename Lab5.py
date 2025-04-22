def hex_char_decode(digit):
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    return hex_map[digit.lower()]


def hex_string_decode(hex):
    if hex.startswith('0x'):
        hex = hex[2:]

    decimal_value = 0
    for i, char in enumerate(reversed(hex)):
        decimal_value += hex_char_decode(char) * (16 ** i)

    return decimal_value


def binary_string_decode(binary):
    if binary.startswith('0b'):
        binary = binary[2:]

    decimal_value = 0
    for i, char in enumerate(reversed(binary)):
        decimal_value += int(char) * (2 ** i)

    return decimal_value


def binary_to_hex(binary):
    if binary.startswith('0b'):
        binary = binary[2:]

    binary = binary.zfill(len(binary) + (4 - len(binary) % 4) % 4)

    bin_to_hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'b', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'f'
    }

    hex_str = ''
    for i in range(0, len(binary), 4):
        four_bits = binary[i:i + 4]
        hex_str += bin_to_hex_map[four_bits]

    return hex_str


def display_menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")


def main():
    while True:
        display_menu()
        choice = input("Please enter an option: ")

        if choice == '1':
            hex_str = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(hex_str)
            print(f"Result: {result}")

        elif choice == '2':
            bin_str = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(bin_str)
            print(f"Result: {result}")

        elif choice == '3':
            bin_str = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(bin_str)
            print(f"Result: {result}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
