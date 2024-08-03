import pickle
from address_book import AddressBook
from handlers import add_contact, change_phone, show_phone, show_all, add_birthday, show_birthday, birthdays
from utils import parse_input


# def parse_input(user_input):
#     parts = user_input.split(maxsplit=1)
#     command = parts[0].lower()
#     args = parts[1].split() if len(parts) > 1 else []
#     return command, args


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


# Функция для загрузки данных
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = book = load_data()
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                save_data(book)
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, book))

            elif command == "change":
                print(change_phone(args, book))

            elif command == "phone":
                print(show_phone(args, book))

            elif command == "all":
                print(show_all(book))

            elif command in ["add-birthday", "add_birthday"]:
                print(add_birthday(args, book))

            elif command in ["show-birthday", "show_birthday"]:
                print(show_birthday(args, book))

            elif command in ["birthdays", "upcoming_birthdays"]:
                print(birthdays(args, book))

            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        save_data(book)


if __name__ == "__main__":
    main()
