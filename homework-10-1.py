from collections import UserDict

class Field():
    def __init__(self, value) -> None:
        self.value = value

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Record():
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone_list = []

    def add_phone(self, phone: Phone):
        self.phone_list.append(phone.phone)
        return  f'Phone {phone.phone} for {self.name.value} added'

    def del_phone(self, phone: Phone):
        if phone.phone in self.phone_list:
            self.phone_list.remove(phone.phone) 
        
        return  f'Phone {phone.phone} for contact {self.name.value} deleted'

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone.phone in self.phone_list:
            self.phone_list.remove(old_phone.phone)
            self.phone_list.append(new_phone.phone)       
        return f'Old number {old_phone.phone} for {self.name.value} has been replaced with a number {new_phone.phone}'
             

class AdressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f'Contact {record.name.value} added'



name = Name('Y')
phone_1 = Phone("09583787827")
phone_2 = Phone('9760293139')
phone_3 = Phone('0667069948')
record = Record(name, phone_1)
ad_book = AdressBook()
print(record.add_phone(phone_1))
print(record.add_phone(phone_2))
#print(record.name.name)

print(record.name.value, record.phone_list)
print(record.change_phone(phone_1, phone_3))
print(record.name.value, record.phone_list)
print(record.del_phone(phone_2))
print(record.name.value, record.phone_list)
print(ad_book.add_record(record))
print(ad_book)