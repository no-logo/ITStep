class ContactsModel:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number):
        id = len(self.contacts) + 1
        self.contacts.append({"ID":id, "first_name":first_name, "last_name":last_name, "phone_number":phone_number})

    def remove_contact(self, id):
        for i in range(len(self.contacts)):
            if self.contacts[i]["ID"] == id:
                print(i)
                self.contacts.pop(i)
class ContactsView:
    
    @staticmethod
    def view_cotntacts(contacts):
        for d in contacts:
            print(d)

class ContactsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_contact(self, first_name, last_name, phone_number):
        self.model.add_contact(first_name, last_name, phone_number)

    def remove_contact(self, id):
        self.model.remove_contact(id)

    def view_contacts(self):
        self.view.view_cotntacts(self.model.contacts)


if __name__ == "__main__":
    model = ContactsModel()
    view = ContactsView()
    
    controller = ContactsController(model, view)

    controller.view_contacts()
    controller.add_contact('Andrzej', 'Wawryk', 1234566)
    #controller.view_contacts()
    controller.add_contact('Maciek', 'Wawryk', 789456)
    controller.view_contacts()
    controller.remove_contact(1)
    #controller.view_contacts()