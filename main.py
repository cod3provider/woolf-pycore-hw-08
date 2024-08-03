from storage import save_data, load_data
from handlers import add_contact, change_phone, show_phone, show_all, add_birthday, show_birthday, birthdays
from utils import parse_input


def main():
    book = load_data()
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
