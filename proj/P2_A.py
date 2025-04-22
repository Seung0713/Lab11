import console_gfx

# ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

def display_menu():
    print("\nRLE Menu\n"
          "--------")
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


def main():
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        display_menu()
        option = int(input("Select a Menu Option:"))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter the name of the file: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data is loaded")
        elif option == 6:
            console_gfx.display_image(image_data)


if __name__ == "__main__":
    main()