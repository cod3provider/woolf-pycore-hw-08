from field import Field


class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value)
