from collections import UserDict
from record import Record
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Only Record instances can be added")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")

    def get_upcoming_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year)
                if today <= bday_this_year <= today + timedelta(days=days):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays
