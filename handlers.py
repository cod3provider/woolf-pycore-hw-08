from address_book import AddressBook
from record import Record


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)

    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return "Contact not found."


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return f"Phones for {name}: {', '.join(phone.value for phone in record.phones)}"
    return "Contact not found."


@input_error
def show_all(book: AddressBook):
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide both args, the contact name and the birthday date in format DD.MM.YYYY."

    name, birthday = args[0], args[1]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_birthday(birthday)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"Birthday of {name} is on {record.birthday}."
    return "Birthday not found for this contact."


@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join(f"{record.name.value}: {record.birthday}" for record in upcoming_birthdays)
    return "No birthdays in the next 7 days."
