grocery_list = []

def add_to_list():
    product = input("What would you like to add to the grocery list? ").lower
    if type(product) != str:
        print("Unexpected input, try again.")
    grocery_list.append(product)

def remove_from_list():
    grocery_list.remove

def list_search():
    for item in grocery_list:
        print(f"These are the contents: {item}")

def main():
    while True:
        print("1. Add an item to the list")
        print("2. Remove an item from the list")
        print("3. Show all the list's items")
        print("4. Leave.")
        option = input("What would you like to do to the list? ")
        if option == "1":
            add_to_list()
        elif option == "2":
            remove_from_list()
        elif option == "3":
            list_search()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()