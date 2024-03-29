from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass # реалізація класу

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone_number(value):
            raise ValueError("Invalid phone number format")
        self.value = value
        
    @staticmethod
    def validate_phone_number(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
        
    def delete_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]
        
    def edit_phone(self, old_phone_number, new_phone_number):
        for i, _ in enumerate(self.phones):
            if str(self.phones[i]) == old_phone_number:
                self.phones[i] = Phone(new_phone_number)
                break

    def find_phone(self, user_name):
        for phone in self.phones:
            if phone.value == user_name:
                return phone.value
        raise ValueError("Phone number not found")


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        return(self.data.get(value))

    def delete(self, name):
        del self.data[name]



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

for name, record in book.data.items():
    print(record)