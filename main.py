from insured import Insured
from insured_collection import InsuredCollection

def create_insured():
    name = input("Zadejte jméno pojištěného: ")
    surname = input("Zadejte příjmení pojištěného: ")
    age = input("Zadejte věk pojištěného: ")
    phone = input("Zadejte telefonní číslo pojištěného: ")
    return Insured(name, surname, age, phone)

def print_menu():
    print("1. Vytvořit pojištěného")
    print("2. Zobrazit seznam pojištěných")
    print("3. Najít pojištěného")
    print("4. Ukončit program")

def main():
    insured_collection = InsuredCollection()
    while True:
        print_menu()
        choice = input("Vyberte možnost: ")
        if choice == "1":
            insured = create_insured()
            insured_collection.add_insured(insured)
            print("Data uložena. Pokračujte libovolnou klávesnicí...")
            input()
        elif choice == "2":
            print(insured_collection)
            input("Pro pokračování stiskněte libovolnou klávesu...")
        elif choice == "3":
            name = input("Zadejte jméno pojištěného: ")
            surname = input("Zadejte příjmení pojištěného: ")
            insured = insured_collection.find_insured_by_name(name, surname)
            if insured is not None:
                print(insured)
            else:
                print("Pojištěný nenalezen.")
                input("Pro pokračování stiskněte libovolnou klávesu...")
        elif choice == "4":
            break
        else:
            print("Neplatná volba. Zvolte 1-4.")
            input("Pro pokračování stiskněte libovolnou klávesu...")

if __name__ == "__main__":
    main()
