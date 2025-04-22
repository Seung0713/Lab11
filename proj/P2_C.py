import console_gfx


# ================================
# Helper Functions
# ================================

def to_hex_string(data):
    """Converts data (RLE or raw) to a hexadecimal string."""
    return ''.join(f'{num:x}' for num in data)


def count_runs(flat_data):
    """Returns the number of runs of data."""
    if not flat_data:
        return 0

    runs = 1
    count = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1] and count < 15:
            count += 1
        else:
            runs += 1
            count = 1
    return runs


def encode_rle(flat_data):
    """Encodes raw data using run-length encoding (RLE)."""
    if not flat_data:
        return []

    encoded_data = []
    count = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1] and count < 15:
            count += 1
        else:
            encoded_data.extend([count, flat_data[i - 1]])
            count = 1
    encoded_data.extend([count, flat_data[-1]])
    return encoded_data


def get_decoded_length(rle_data):
    """Returns the decompressed size of RLE data."""
    return sum(rle_data[i] for i in range(0, len(rle_data), 2))


def decode_rle(rle_data):
    """Decodes RLE-encoded data back to raw data."""
    decoded_data = []
    for i in range(0, len(rle_data), 2):
        run_length = rle_data[i]
        value = rle_data[i + 1]
        decoded_data.extend([value] * run_length)
    return decoded_data


def string_to_data(data_string):
    """Converts a hexadecimal string into byte data."""
    return [int(data_string[i], 16) for i in range(len(data_string))]


def to_rle_string(rle_data):
    """Converts RLE data into a human-readable string."""
    rle_string = []
    for i in range(0, len(rle_data), 2):
        rle_string.append(f"{rle_data[i]}{format(rle_data[i + 1], 'x')}")
    return ':'.join(rle_string)


def string_to_rle(rle_string):
    """Converts a human-readable RLE string into byte data."""
    rle_data = []
    runs = rle_string.split(':')
    for run in runs:
        length = int(run[:-1])
        value = int(run[-1], 16)
        rle_data.extend([length, value])
    return rle_data


# ================================
# Main Program Menu
# ================================

def main():
    """Main menu and driver for the RLE encoder/decoder."""
    image_data = []
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    print("\n")

    while True:
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        print()

        option = input("Select a Menu Option: ")

        if option == "0":
            break

        elif option == "1":
            filename = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(filename)
            print("File loaded.\n")

        elif option == "2":
            image_data = console_gfx.test_image
            print("Test image data loaded.\n")

        elif option == "3":
            rle_string = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_string))
            print("RLE data decoded.\n")

        elif option == "4":
            hex_string = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(hex_string))
            print("RLE hex data decoded.\n")

        elif option == "5":
            flat_hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(flat_hex_string)
            print("Flat data loaded.\n")

        elif option == "6":
            if image_data:
                console_gfx.display_image(image_data)
            else:
                print("No image data loaded.\n")

        elif option == "7":
            if image_data:
                encoded_data = encode_rle(image_data)
                print(f"RLE representation: {to_rle_string(encoded_data)}\n")
            else:
                print("No image data loaded.\n")

        elif option == "8":
            if image_data:
                encoded_data = encode_rle(image_data)
                print(f"RLE hex values: {to_hex_string(encoded_data)}\n")
            else:
                print("No image data loaded.\n")

        elif option == "9":
            if image_data:
                print(f"Flat hex values: {to_hex_string(image_data)}\n")
            else:
                print("No image data loaded.\n")

        else:
            print("Invalid option. Please select a valid option.\n")


# Run main
if __name__ == "__main__":
    main()
