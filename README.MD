### Technical Task Description

#### Task 1

First, we will add additional functionality to the classes from the previous homework:

- Add a `birthday` field to the `Record` class for the birthday. This field should be of the `Birthday` class. This field is optional, but there can only be one.

```
class Birthday(Field):
    def __init__(self, value):
        try:
            # Add data validation
            # and convert the string to a datetime object
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
```

```
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
```

- Add functionality to work with `Birthday` in the `Record` class, specifically a function `add_birthday` that adds a birthday to the contact.
- Add functionality to validate the values provided for the `Phone` and `Birthday` fields.
- Add and adapt our function from the fourth homework, week 3, `get_upcoming_birthdays`, to the `AddressBook` class. This function should return a list of users to be congratulated by days over the next week.

Now your bot should work with the functionality of the `AddressBook` class. This means that instead of the `contacts` dictionary, we use `book = AddressBook()`.

#### Task 2

To implement the new functionality, also add handler functions with the following commands:

- `add-birthday` - add a birthday to the contact in the format DD.MM.YYYY
- `show-birthday` - show the birthday of the contact
- `birthdays` - returns a list of users who need to be congratulated by days over the next week

```
@input_error
def add_birthday(args, book):
    # implementation

@input_error
def show_birthday(args, book):
    # implementation

@input_error
def birthdays(args, book):
    # implementation
```

So, in the end, our bot should support the following list of commands:

1. `add [name] [phone]`: Add a new contact with a name and phone number, or a phone number to an existing contact.
2. `change [name] [old phone] [new phone]`: Change the phone number for the specified contact.
3. `phone [name]`: Show the phone numbers for the specified contact.
4. `all`: Show all contacts in the address book.
5. `add-birthday [name] [birthday]`: Add a birthday for the specified contact.
6. `show-birthday [name]`: Show the birthday for the specified contact.
7. `birthdays`: Show the birthdays that will occur over the next week.
8. `hello`: Get a greeting from the bot.
9. `close` or `exit`: Close the program.

```
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # implementation

        elif command == "change":
            # implementation

        elif command == "phone":
            # implementation

        elif command == "all":
            # implementation

        elif command == "add-birthday":
            # implementation

        elif command == "show-birthday":
            # implementation

        elif command == "birthdays":
            # implementation

        else:
            print("Invalid command.")
```

For example, let's consider the implementation of the `add [name] [phone]` command. In the `main` function, we need to add the handling of this command in the appropriate place:

```
elif command == "add":
    print(add_contact(args, book))
```

The implementation of the `add_contact` function might look like this:

```
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
```

Our `add_contact` function has two purposes - adding a new contact or updating the phone number for an existing contact in the address book. 

The function parameters are a list of arguments `args` and the address book `book`. 
- First, the function unpacks the `args` list, obtaining the `name` and `phone` from the first two elements of the list. The remaining arguments are ignored using `*_`. Then, the `find` method of the `book` object searches for a record with the `name`. If a record with such a name exists, the method returns this record, otherwise `None` is returned.
- If the record is not found, it is a new contact and the function creates a new `Record` object with the `name` and adds it to the `book` by calling the `add_record` method. After adding the new record, the variable `message` is assigned the message "Contact added." to indicate the success of the operation.
- Then, regardless of whether the record was found or a new one was created, the phone number is added to this record using the `add_phone` method if it was provided. Finally, the function returns a message about the result of its work: "Contact updated." if the contact was updated, or "Contact added." if the contact was added. To catch input errors and output the appropriate error message, we use the `@input_error` decorator.

### Evaluation Criteria:

1. Implement all the specified commands for the bot.
2. All data should be output in a clear and user-friendly format.
3. All errors, such as incorrect input or missing contact, should be handled informatively with the appropriate message to the user.
4. Data validation:
    - The birthday must be in the format DD.MM.YYYY.
    - The phone number must consist of 10 digits.
5. The program should close correctly after executing the `close` or `exit` commands.