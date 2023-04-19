class Insured:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.phone}"
