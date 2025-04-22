import sys
from heifer_generator import get_cows
from dragon import Dragon

def list_cows(cows):
    cow_names = [cow.get_name() for cow in cows]
    print(f"Cows available: {' '.join(cow_names)}")

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def main():
    cows = get_cows()

    if len(sys.argv) == 1:
        print("Usage: python cowsay.py [-l] [-n COW] MESSAGE")
        return

    if sys.argv[1] == "-l":
        list_cows(cows)
        return
    elif sys.argv[1] == "-n":
        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])
        cow = find_cow(cow_name, cows)

        if cow is None:
            print(f"Could not find {cow_name} cow!")
        else:
            print(message)
            print(cow.get_image())

            if isinstance(cow, Dragon):
                if cow.can_breath_fire():
                    print("\nThis dragon can breathe fire.")
                else:
                    print("\nThis dragon cannot breathe fire.")
    else:
        message = " ".join(sys.argv[1:])
        default_cow = find_cow("heifer", cows)
        print(message)
        image = [cow.image for cow in get_cows()]
        print(image[0])

if __name__ == "__main__":
    main()
