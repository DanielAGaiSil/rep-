grocery_list = ["apple"]


def add_to_list():
    product = input("What would you like to add to the grocery list?")
    grocery_list.append(product)

def remove_list():
    grocery_list.remove()

def list_search():
    for _ in grocery_list:
        print(f"These are the contents: {_}")

list_search()