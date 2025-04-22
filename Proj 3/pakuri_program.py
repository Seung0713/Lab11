from pakudex import Pakudex

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                print("Please enter a valid size.")
            else:
                break
        except ValueError:
            print("Please enter a valid size.")

    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.\n")

    while True:
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")

        choice = input("What would you like to do? ")

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Unrecognized menu selection!\n")
            continue

        if choice == "1":
            species_array = pakudex.get_species_array()
            if not species_array:
                print("No Pakuri in Pakudex yet!\n")
            else:
                print("Pakuri In Pakudex:")
                for idx, species in enumerate(species_array, start=1):
                    print(f"{idx}. {species}")
                print()

        elif choice == "2":
            species = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species)
            if stats:
                print(f"Species: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}\n")
            else:
                print("Error: No such Pakuri!\n")

        elif choice == "3":
            if pakudex.get_size() >= pakudex.get_capacity():
                print("Error: Pakudex is full!\n")
            else:
                species = input("Enter the name of the species to add: ")
                success = pakudex.add_pakuri(species)
                if success:
                    print(f"Pakuri species {species} successfully added!\n")
                else:
                    print("Error: Pakudex already contains this species!\n")

        elif choice == "4":
            species = input("Enter the name of the species to evolve: ")
            success = pakudex.evolve_species(species)
            if success:
                print(f"{species} has evolved!\n")
            else:
                print("Error: No such Pakuri!\n")

        elif choice == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!\n")

        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break

if __name__ == "__main__":
    main()
