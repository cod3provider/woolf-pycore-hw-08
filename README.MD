**Technical Task Description**

☝ In this homework assignment, you are required to add functionality for saving the address book to disk and restoring it from disk.

To achieve this, you should use the pickle protocol for data serialization/deserialization and implement methods that allow saving all data to a file and loading it from a file.

The main goal is to ensure that the application does not lose data after exiting and that upon restarting, it can restore the data from the file. The address book you worked with in the previous session should be preserved.

Implement the functionality to save the state of the AddressBook to a file when the program closes and to restore the state when it starts.

**Code examples that may be helpful:**

*Serialization with pickle*
```
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Returns a new address book if the file is not found
```

*Integrating saving and loading into the main loop*
```
def main():
    book = load_data()

    # Main program loop

    save_data(book)  # Call this before exiting the program
```

These examples will help you in completing the homework assignment.

**Evaluation Criteria:**

- The data serialization/deserialization protocol using pickle is implemented.
- All data should be saved when the program exits.
- Upon starting a new session, the address book in the application should be the one from the previous session.