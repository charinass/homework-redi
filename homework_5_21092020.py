class Restaurant_staff:
    def __init__(self, name, phone, email, address, salary
                 ):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.salary = salary
    '''
    Normal restaurant staff data
    '''


class Chef(Restaurant_staff):
    def __init__(self, name, phone, email, address, salary, cuisine_expertise):
        super().__init__(name, phone, email, address, salary)
        self.cuisine_expertise = cuisine_expertise

    def take_dish_name(self, customer):
        print(
            f"Chef {self.name} takes {customer.name}'s order = {customer.order}.")

    def prep_dish(self, server, customer):
        print(
            f"Chef {self.name} prepares {customer.name}'s order = {customer.order} from Server {server.name}.")


class Restaurant_manager(Restaurant_staff):
    def __init__(self, name, phone, email, address, salary):
        super().__init__(name, phone, email, address, salary)

    def staff_payroll(self, server, chef):
        '''
        Records of staff info and staff base salary
        '''
        print(
            f"Staff payroll:" +
            f"\nRestaurant manager = {self.salary} \nServer = {server.salary}, \nChef = {chef.salary}")

    def calculate_billing(self, customer):
        '''
        Calculates total customer order bill from customer.order
        '''
        total_bill = sum([float(value)
                          for key, value in customer.order.items()])
        print(
            f"Restaurant manager calculates customer {customer.name}'s bill")
        return total_bill

    def provide_bill(self, customer):
        print(
            f"Manager {self.name} provides customer {customer.name}'s bill: %.2f" % customer.total_bill)


class Servers(Restaurant_staff):
    def __init__(self, name, phone, email, address, salary):
        super().__init__(name, phone, email, address, salary)

    def fulfill_book_table_request(self, customer):
        print(f"Table is booked under {customer.name}.")

    def take_customer_order(self, customer):
        print(f"Server {self.name} takes customer {customer.name}'s order.")
        self.send_order_to_kitchen(customer)

    def send_order_to_kitchen(self, customer):
        print(
            f"Server {self.name} sends {customer.name}'s order to the kitchen = {customer.order}")


class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def send_book_table_request(self, server):
        '''
        Sends table request to Servers.fulfill_book_table_request()
        '''
        print("Customer made request for a table.")
        server.fulfill_book_table_request(self)

    def give_order(self, server):
        # self.order = {input("order:"): input("amount:")}
        #self.order.update({input("order:"): input("amount:")})
        self.order = {"spaghetti bolognese": 10.50, "red wine": 9.00, }
        print(f"{self.name} orders {self.order}.")
        # return self.order

    def ask_bill(self, total_bill):
        print("Customer asks for the total bill.")
        self.total_bill = total_bill


if __name__ == "__main__":
    '''
    sample
    '''
    _customer = Customer(
        "Foodie", "123-456-7890", "foodie@myemail.com")
    _server = Servers("John", "123-456-7890",
                      "john@smith.com", "#10 Notting Hill", "$45,000")
    _chef = Chef("Nemo", "098-765-4321", "nemo@thegreatbarrierreef.com",
                 "The Great Barrier Reef, Australia", "$50,000", "Fish dishes")
    _restaurant_mgr = Restaurant_manager(
        "Python", "234-567-8901", "python@amazon.com", "The Amazonian Forest", "$55,000")

    _customer.send_book_table_request(_server)
    _customer.give_order(_server)

    _server.take_customer_order(_customer)

    _chef.prep_dish(_server, _customer)

    _restaurant_mgr.staff_payroll(_server, _chef)
    total_bill = _restaurant_mgr.calculate_billing(_customer)

    _customer.ask_bill(total_bill)
    _restaurant_mgr.provide_bill(_customer)
