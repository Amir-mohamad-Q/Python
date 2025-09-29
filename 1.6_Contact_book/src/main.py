from collections import defaultdict


class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, phone, name, email=None):
        if name in self.contacts:
            print("contact Already exist")
            return
        
        self.contacts[phone]["name"] = name 
        self.contacts[phone]["email"] = email 

    def view_contac(self,):
        for phone, info in self.contacts.items():
            print(f"Phone: {phone} Name: {info["name"]} email: {info["email"]}\n{"----" * 13}")

    def delete_contact(self, phone):
        if phone in self.contacts:
            print(f"contact ({self.contacts[phone]["name"]}:{phone}) deleted!")
            del self.contacts[phone]

    def update_contact(self, phone, name=None, email=None):
        if phone in self.contacts:
            if name:
                self.contacts[phone]["name"] = name
            else:
                self.contacts[phone]["name"] = ''
            if email:
                self.contacts[phone]["email"] = email
            else:
                self.contacts[phone]["email"] = ''
            print("contact updated successfully!")
            return
        

if __name__ == "__main__":
    book = ContactBook()
    book.add_contact("09164562010","amir","amir@gmail.com")
    while True:
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View Contact")
        print("5. Quit Contact\n\n")

        user_choice = input("Enter a number")

        if user_choice == '5':
            break
        elif user_choice == '1':
            phone = input("Enter a Phone: ")
            name = input("Enter a Name: ")
            email = input("Enter a Email: ")

            book.add_contact(phone, name, email)

        elif user_choice == '2':
            phone = input("Enter a Phone: ")
            name = input("Enter a Name: ")
            email = input("Enter a Email: ")

            book.update_contact(phone, name, email)

        elif user_choice == '3':
            phone = input("Enter a phone number: ")
            book.delete_contact(phone)
            
        elif user_choice == '4':
            print(book.view_contac())