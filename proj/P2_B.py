import console_gfx


# Part A: Menu and Image Display

def display_menu():
    print("Welcome to the Image RLE Compression Program!")
    print("1. Load Image from File")
    print("2. Load Test Image")
    print("3. Display Image")
    print("4. Display RLE String")
    print("5. Display RLE Hex Data")
    print("6. Display Flat Hex Data")
    print("7. Encode and Display Image in RLE")
    print("8. Decode RLE and Display Image")
    print("9. Exit")


def main():
    image_data = None
    rle_data = None

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            filename = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(filename)
            print("Image loaded.")

        elif choice == "2":
            image_data = console_gfx.test_image()
            print("Test image data loaded.")

        elif choice == "3":
            if image_data:
                console_gfx.display_image(image_data)
            else:
                print("No image loaded.")

        elif choice == "4":
            if rle_data:
                print(f"RLE representation: {to_rle_string(rle_data)}")
            else:
                print("No RLE data available.")

        elif choice == "5":
            if rle_data:
                print(f"RLE hex values: {to_hex_string(rle_data)}")
            else:
                print("No RLE data available.")

        elif choice == "6":
            if image_data:
                flat_data = encode_rle(image_data)  # Convert image_data to RLE first
                print(f"Flat hex values: {to_hex_string(flat_data)}")
            else:
                print("No image loaded.")

        elif choice == "7":
            if image_data:
                rle_data = encode_rle(image_data)
                print(f"Encoded RLE: {to_rle_string(rle_data)}")
            else:
                print("No image loaded.")

        elif choice == "8":
            if rle_data:
                decoded_data = decode_rle(rle_data)
                console_gfx.display_image(decoded_data)
            else:
                print("No RLE data available.")

        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


# Part B: Core Methods for RLE Encoding and Decoding

def to_hex_string(data):
    return ''.join(format(x, 'x') for x in data)


def count_runs(flat_data):
    runs = 0
    current_run_value = flat_data[0]
    current_run_length = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == current_run_value and current_run_length < 15:
            current_run_length += 1
        else:
            runs += 1
            current_run_value = flat_data[i]
            current_run_length = 1
    runs += 1
    return runs


def encode_rle(flat_data):
    rle_data = []
    count = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1] and count < 15:
            count += 1
        else:
            rle_data.extend([count, flat_data[i - 1]])
            count = 1
    rle_data.extend([count, flat_data[-1]])  # Add the last run
    return rle_data


def get_decoded_length(rle_data):
    return sum(rle_data[i] for i in range(0, len(rle_data), 2))


def decode_rle(rle_data):
    flat_data = []
    for i in range(0, len(rle_data), 2):
        run_length = rle_data[i]
        value = rle_data[i + 1]
        flat_data.extend([value] * run_length)
    return flat_data


def string_to_data(data_string):
    slist = []
    for i in range(len(data_string)):
        if data_string[i] == 'a':
            slist.append(10)
        elif data_string[i] == 'b':
            slist.append(11)
        elif data_string[i] == 'c':
            slist.append(12)
        elif data_string[i] == 'd':
            slist.append(13)
        elif data_string[i] == 'e':
            slist.append(14)
        elif data_string[i] == 'f':
            slist.append(15)
        else:
            slist.append(int(data_string[i]))
    return slist

def to_rle_string(rle_data):
    return ':'.join([f"{run}:{hex(value)[2:]}" for run, value in zip(rle_data[::2], rle_data[1::2])])


def string_to_rle(rle_string):
    parts = rle_string.split(':')
    rle_data = []
    for i in range(0, len(parts), 2):
        rle_data.append(int(parts[i]))
        rle_data.append(int(parts[i + 1], 16))
    return rle_data


# Part C: Integration and Execution

if __name__ == "__main__":
    main()
