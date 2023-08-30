import re
import json
from datetime import datetime

customers = []
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def display_menu():

    print("1. List all customers")
    print("2. Search customers")
    print("3. Add new customer")
    print("4. Update existing customer")
    print("5. Delete existing customer")
    print("6. Load")
    print("7. Save")
    print("8. Exit")
    print()


def list_customers():
    if len(customers) > 0:
        for index, c in enumerate(customers):
            print(index, "=", c)
    else:
        print("No customers found")


def search_customers():
    if len(customers) == 0:
        print("No customers found")
    else:
        while True:
            search_field = input(
                "Type 1 --> search customer name, 2 --> telephone, 3 --> email: ").strip()
            if search_field.isalpha() or int(search_field) not in [1, 2, 3]:
                print("Invalid input. Please select 1, 2 or 3: ")
            else:
                search_query = input("Search value: ").lower().strip()
                search_results = []

                for c in customers:
                    if int(search_field) == 1 and c.get("name") == search_query:
                        search_results.append(c)
                    elif int(search_field) == 2 and c.get("telephone") == search_query:
                        search_results.append(c)
                    elif int(search_field) == 3 and c.get("email") == search_query:
                        search_results.append(c)

                if not search_results:
                    print()
                    print("Could not find any matching customers.")
                    return
                else:
                    for c in search_results:
                        print()
                        print("Customer name: ", c["name"])
                        print("Telephone: ", c["telephone"])
                        print("Customer email: ", c["email"])
                        return


def add_customer():
    customer = {}

    while True:
        customer_name = input("Customer name: ").strip()
        if customer_name != "" and customer_name.isalpha():
            customer["name"] = customer_name
            break
        else:
            print("Invalid name input")

    while True:
        customer_telephone = input("Telephone: ").strip()
        if customer_telephone != "" and customer_telephone.isnumeric():
            customer["telephone"] = customer_telephone
            break
        else:
            print("Invalid telephone input")

    while True:
        customer_email = input("Email: ").strip()
        if customer_email != "" and re.fullmatch(email_regex, customer_email):
            customer["email"] = customer_email
            break
        else:
            print("Invalid email input")

    print("Newly added: ", customer)
    customers.append(customer)


def update_customer():
    if len(customers) == 0:
        print("No customer found")
    else:
        list_customers()
        customer = input("Select entry to update: ").strip()

        if customer.isalpha() or int(customer) < 0 or int(customer) >= len(customers):
            print("Invalid customer selected")
            return
        else:

            while True:
                new_customer_name = input(
                    "Updated customer name: ").strip()
                if new_customer_name != "" and new_customer_name.isalpha():
                    customers[int(customer)]["name"] = new_customer_name
                    break
                else:
                    print("Invalid name input")

            while True:
                new_customer_telephone = input(
                    "Updated customer telephone: ").strip()
                if new_customer_telephone != "" and new_customer_telephone.isnumeric():
                    customers[int(customer)
                              ]["telephone"] = new_customer_telephone
                    break
                else:
                    print("Invalid telephone input")

            while True:
                new_customer_email = input(
                    "Updated customer email: ").strip()
                if new_customer_email != "" and re.fullmatch(email_regex, new_customer_email):
                    customers[int(customer)]["email"] = new_customer_email
                    break
                else:
                    print("Invalid email input")

            print("Updated details:", customers[int(customer)])


def delete_customer():
    list_customers()
    while True:
        customer = input("Select entry to delete: ").strip()
        if customer.isalpha() or int(customer) >= len(customers):
            print("Invalid customer selected")
        else:
            del customers[int(customer)]
            print("Entry deleted successfully")
            break


def load_data():
    with open("dummy_data.json", "r") as json_file:
        data = json.load(json_file)
        customers.clear()
        for c in data:
            customers.append(c)


def save_data():
    with open('dummy_data_copy.json', "w") as output_file:
        json.dump(customers, output_file)


def main():
    while True:
        print()
        print(datetime.now())
        display_menu()
        user_input = input("Select an option: ").strip()
        if user_input == "1":
            print()
            list_customers()
        elif user_input == "2":
            print()
            search_customers()
        elif user_input == "3":
            print()
            add_customer()
        elif user_input == "4":
            print()
            update_customer()
        elif user_input == "5":
            print()
            delete_customer()
        elif user_input == "6":
            print("Loading data...")
            print()
            load_data()
        elif user_input == "7":
            print("Saving...")
            print()
            save_data()
        elif user_input == "8":
            print("Goodbye!")
            print()
            break
        else:
            print("Invalid input")
            print()


if __name__ == "__main__":
    main()
