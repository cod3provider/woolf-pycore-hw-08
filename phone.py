import re
from field import Field


class Phone(Field):
    def __init__(self, value):
        if not self._is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def _is_valid_phone(value):
        return re.fullmatch(r'\d{10}', value) is not None